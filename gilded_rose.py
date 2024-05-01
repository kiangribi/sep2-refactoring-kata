# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            quality_drain = 1
            if item.name == "Aged Brie":
                quality_drain = -1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    quality_drain = 0
                elif item.sell_in <= 5:
                    quality_drain = 3
                elif item.sell_in <= 10:
                    quality_drain = 2
            if item.sell_in < 0:
                quality_drain = 2

            item.sell_in -= 1
            item.quality = min(max(quality_drain, 0), 50)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
