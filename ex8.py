# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
# so print what? I think none. But,it prints "%r %r %r %r"
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# why give me so many strings?
print formatter % (
	u"《江雪》",
	u"唐·柳宗元",
	u"千山鸟飞绝，万径人踪灭。",
	u"孤舟蓑笠翁，独钓寒江雪。"
)