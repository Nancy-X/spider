# -*- coding: utf-8 -*-

from scrapy import Item,Field
class TodaynewsItem(Item):
    name = scrapy.Field()
	abstract=Field()
	article_genre=Field()
	behot_time=Field()
	chinese_tag=Field()
	comments_count=Field()
	group_id=Field()
	group_source=Field()
	has_gallery=Field()
	image_list=Field()
	image_url=Field()
	is_feed_ad=Field()
	label=Field()
	media_avatar_url=Field()
	media_url=Field()
	middle_mode=Field()
	more_mode=Field()
	single_mode=Field()
	source=Field()
	source_url=Field()
	tag=Field()
	tag_url=Field()
	title=Field()
	pass