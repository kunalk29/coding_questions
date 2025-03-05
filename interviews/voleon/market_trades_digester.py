import math
from typing import Any, Dict, List, Optional, Tuple

MINUTE_IN_SECONDS = 60


class Trade:
    timestamp: int
    security: str
    quantity: int
    price: int
    client: str
    order_timestamp: Optional[int]

    def __init__(
            self,
            timestamp: int,
            security: str,
            quantity: int,
            price: int,
            client: str,
            order_timestamp: Optional[int]
    ) -> None:
        self.timestamp = timestamp
        self.security = security
        self.quantity = quantity
        self.price = price
        self.client = client
        self.order_timestamp = order_timestamp


class Order:
    timestamp: int
    security: str
    client: str
    goal_shares: int
    participation_rate: float
    current_fill: int

    def __init__(
            self,
            timestamp: int,
            security: str,
            client: str,
            goal_shares: int,
            participation_rate: float
    ) -> None:
        self.timestamp = timestamp
        self.security = security
        self.client = client
        self.goal_shares = goal_shares
        self.participation_rate = participation_rate
        self.current_fill = 0


class MarketDataIngester:
    trade_map: Dict[str, List[Trade]] = {}
    order_map: Dict[str, Dict[str, Order]] = {}

    def __init__(self) -> None:
        pass

    def ingest_trade(self, timestamp: int, security: str, quantity: int, price: int, client: str,
                     order_timestamp: int) -> None:
        if security in self.trade_map.keys():
            self.trade_map[security].append(
                Trade(
                    timestamp=timestamp,
                    quantity=quantity,
                    security=security,
                    price=price,
                    client=client,
                    order_timestamp=order_timestamp
                )
            )
        else:
            self.trade_map[security] = [
                Trade(
                    timestamp=timestamp,
                    quantity=quantity,
                    security=security,
                    price=price,
                    client=client,
                    order_timestamp=order_timestamp
                )
            ]

    def add_order(
            self,
            timestamp: int,
            security: str,
            client: str,
            goal_shares: int,
            participation_rate: float
    ) -> None:
        if client not in self.order_map.keys():
            self.order_map[client] = {
                security: Order(
                    timestamp=timestamp,
                    security=security,
                    client=client,
                    goal_shares=goal_shares,
                    participation_rate=participation_rate
                )
            }
        else:
            self.order_map[client][security] = Order(
                timestamp=timestamp,
                security=security,
                client=client,
                goal_shares=goal_shares,
                participation_rate=participation_rate
            )

    def generate_volume_check(self, timestamp: int, security: str) -> Tuple[int, int]:
        if security not in self.trade_map.keys():
            return 0, 0
        all_valid_trades = []
        ind = len(self.trade_map[security]) - 1
        while self.trade_map[security][ind].timestamp > timestamp - MINUTE_IN_SECONDS and ind >= 0:
            all_valid_trades.append(self.trade_map[security][ind])
            ind -= 1
        if not all_valid_trades:
            return 0, 0
        last_price = all_valid_trades[0].price
        volume = sum([x.quantity for x in all_valid_trades])
        return volume, last_price

    def print_volume_check(self, timestamp: int, security: str) -> None:
        volume, last_price = self.generate_volume_check(timestamp=timestamp, security=security)
        if volume == 0:
            print(f"traded-volume {timestamp} {security} 0 NA")
        else:
            print(f"traded-volume {timestamp} {security} {volume} {last_price}")

    def process_order(self, timestamp: int, security: str, quantity: int, price: int) -> None:
        market_volume, last_price = self.generate_volume_check(timestamp=timestamp, security=security)
        for client in self.order_map.keys():
            if security in self.order_map[client].keys():
                current_order = self.order_map[client][security]
                tradeable_volume = math.floor((
                                                          market_volume - current_order.current_fill) * current_order.participation_rate) - current_order.current_fill
                tradeable_volume = min(current_order.goal_shares, quantity, tradeable_volume)
                if tradeable_volume > 0:
                    print(f"print {timestamp} {security} {tradeable_volume} {last_price}")
                    self.ingest_trade(timestamp=timestamp, security=security, quantity=tradeable_volume,
                                      price=last_price, client=current_order.client,
                                      order_timestamp=current_order.timestamp)
                    self.order_map[client][security].current_fill += tradeable_volume

    @staticmethod
    def order_components_within_second(current_second_events: List[List[Any]]) -> List[List[Any]]:
        trades = [x for x in current_second_events if x[0] == 'print']
        volume_checks = [x for x in current_second_events if x[0] == 'volume-check']
        orders = [x for x in current_second_events if x[0] == 'order']
        return trades + volume_checks + orders

    def kill_old_orders(self, timestamp: int) -> None:
        client_security_pairs = []
        for client in self.order_map.keys():
            for security in self.order_map[client].keys():
                if timestamp >= self.order_map[client][security].timestamp + 60:
                    client_security_pairs.append((client, security))

        for x, y in client_security_pairs:
            self.order_map[x].pop(y)

    def process_events(self, events: List[List[Any]]) -> None:
        for event in events:
            if event[0] == 'print':
                self.ingest_trade(
                    timestamp=int(event[1]),
                    security=event[2],
                    quantity=int(event[3]),
                    price=int(event[4]),
                    client='market',
                    order_timestamp=None
                )
                self.process_order(
                    timestamp=int(event[1]),
                    security=event[2],
                    quantity=int(event[3]),
                    price=int(event[4])
                )
            if event[0] == 'volume-check':
                self.print_volume_check(
                    timestamp=int(event[1]),
                    security=event[2]
                )
            if event[0] == 'order':
                self.add_order(
                    timestamp=int(event[1]),
                    security=event[2],
                    client=event[3],
                    goal_shares=int(event[4]),
                    participation_rate=float(event[5])
                )
                current_volume, last_price = self.generate_volume_check(timestamp=int(event[1]), security=event[2])
                self.process_order(timestamp=int(event[1]), security=event[2], quantity=current_volume,
                                   price=last_price)

    def runner(self) -> None:
        current_second = -1
        current_second_events = []
        try:
            while x := input():
                components = x.split(" ")
                new_timestamp = int(components[1])
                if new_timestamp == current_second:
                    current_second_events.append(components)
                    continue
                else:
                    current_second_events = self.order_components_within_second(current_second_events)
                    self.process_events(events=current_second_events)
                    current_second_events = [components]
                    current_second = new_timestamp
                    self.kill_old_orders(timestamp=new_timestamp)
        except EOFError:
            self.process_events(events=current_second_events)


if __name__ == '__main__':
    market_data_ingester = MarketDataIngester()
    market_data_ingester.runner()