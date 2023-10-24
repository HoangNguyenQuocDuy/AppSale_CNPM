def load_categories():
    return [
        {
            "id": 1,
            "name": 'Điện thoại'
        },
        {
            "id": 2,
            "name": 'Table'
        },
        {
            "id": 3,
            "name": 'Laptop'
        }
    ]


def load_products(kw):
    products = [
        {
            "id": 1,
            "name": 'Iphone 15 titan',
            "price": 35000000,
            'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-blacktitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845694698'
        },
        {
            "id": 2,
            "name": 'Ipad 2022',
            "price": 35000000,
            'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-blacktitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845694698'
        },
        {
            "id": 3,
            "name": 'Iphone 15 titan',
            "price": 35000000,
            'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-blacktitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845694698'
        },
        {
            "id": 4,
            "name": 'Iphone 15 titan',
            "price": 35000000,
            'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-blacktitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845694698'
        }, {
            "id": 5,
            "name": 'Iphone 15 titan',
            "price": 35000000,
            'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-blacktitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845694698'
        }, {
            "id": 6,
            "name": 'Iphone 15 titan',
            "price": 35000000,
            'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-blacktitanium?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1692845694698'
        },
    ]

    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]

    return products
