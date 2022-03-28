# pynyac

A nice text encrytion method for cats.

很适合猫的文本加密方法

Example use:

使用例：

```shell
$ python
>>> from pynyac import nyaencode
>>> nyaencode('有内鬼，终止交易！', 'emoji')
'😿🐱😸😹😼😻😻😿😺🙀😻😹😻😻😻😼😸🐱😹😻😻😿😽🐱🙀🙀😻😻😸😺😼🐱😿😻😻😻😸😿😾😽😻😻😽😹😸😻😽😻😻😸😹😸😼😽😻😻😸🙀😺😾😾😻😻'
```

To decrypt this message, use the decode function:

使用解密函数解密此信息：

```shell
$ python
>>> from pynyac import nyadecode
>>> nyadecode('😿🐱😸😹😼😻😻😿😺🙀😻😹😻😻😻😼😸🐱😹😻😻😿😽🐱🙀🙀😻😻😸😺😼🐱😿😻😻😻😸😿😾😽😻😻😽😹😸😻😽😻😻😸😹😸😼😽😻😻😸🙀😺😾😾😻😻', 'emoji')
'有内鬼，终止交易！'
```

You can create a personal dictionary easily, but, NO duplicated items are accepted, they will cause trouble!

很容易就能创建你的个人字典（准确的说，一个字符列表），但是，不要出现重复的项，这会造成问题。

You only need to modify variable `nya_locales`, e. g.

只需要修改变量`nya_locales`，例如

```python
nya_locales = {
    'my_locale': [
        '❌', '⭕' # at least 2 unicode characters should be provided
    ] # add a personal dictionary
}
```

## List of locales

- zh_cn: Chinese cat
- emoji: emojis with a cat
- bb64: baby64, using the dictionary of base64, for baby cats
- wsp: whitespace characters, for those blind cats (be aware of embeded trojans written in whitespace language)
