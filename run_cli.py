from apparel_orders.core import Order, summarize


if __name__ == "__main__":
    record = Order.create("demo", "v1", "draft", "operator", {"场景": "登记量体订单并生成订单摘要"})
    print(summarize(record))

