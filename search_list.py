"""
    \"단어\"  단어1
    \"단 어\" 단어2
    단|어     단-어
    단*어     단0어
"""

searchKeyWords = {
    '항공기사고':           '항공기사고',
    '항공기^사고':          '항공기^사고',
    '항공기 사고':          '항공기 사고',
    '"항공기사고대책"':     '항공기사고대책1',
    '"항공기사고 대책"':    '항공기사고 대책2',
    '항공기사고*':          '항공기사고0',
    '항공*사고':            '항공0사고',
    '항공기사고|대책':      '항공기사고-대책',
    '위안부':               '위안부',
    '위안부^명부':          '위안부^명부',
    '위안부 명부':          '위안부 명부',
    '"위안부명부"':         '위안부명부1',
    '"위안부 명부"':        '위안부 명부2',
    '위안부*':              '위안부0',
    '위안부*명부':          '위안부0명부',
    '위안*명부':            '위안0명부',
    '위안부 | 명부':        '위안부 - 명부',
    '위안부 |명부':         '위안부 -명부',
    '붕괴사고':             '붕괴사고',
    '붕괴^사고':            '붕괴^사고',
    '붕괴 사고':            '붕괴 사고',
    '"붕괴사고"':           '붕괴사고1',
    '"붕괴 사고"':          '붕괴 사고2',
    '붕괴사고*':            '붕괴사고0',
    '붕괴*사고':            '붕괴0사고',
    '붕*사고':              '붕0사고',
    '붕괴 | 사고':          '붕괴 - 사고',
    '붕괴 |사고':           '붕괴 -사고',
    '휴전협정':             '휴전협정',
    '휴전^협정':            '휴전^협정',
    '휴전 협정':            '휴전 협정',
    '"휴전협정"':           '휴전협정1',
    '"휴전 협정"':          '휴전 협정2',
    '휴전*':                '휴전0',
    '휴전*협정':            '휴전0협정',
    '휴*협정':              '휴0협정',
    '휴전 | 협정':          '휴전 - 협정',
    '휴전 |협정':           '휴전 -협정',
    '항로':                 '항로',
    '항로^공역':            '항로^공역',
    '항로 공역':            '항로 공역',
    '"항로공역"':           '항로공역1',
    '"항로 공역"':          '항로 공역2',
    '항로*':                '항로0',
    '항로*공역':            '항로0공역',
    '항*공역':              '항0공역',
    '항로 | 공역':          '항로 - 공역',
    '항로 |공역':           '항로 -공역'
}