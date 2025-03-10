import re


data = """Хан Ган	2024г.	Кванджу, Южная Корея
Юн Фоссе	2023г.	Хёугесунн, Норвегия
Анни Эрно	2022г.	Лильбонн, Франция
Абдулразак Гурна	2021г.	Занзибар
Луиза Глюк	2020г.	Нью-Йорк
Петер Хандке	2019г.	Гриффен, Австрия
Ольга Токарчук	2018г.	Сулехув, Польша
Кадзуо Исигуро	2017г.	Нагасаки, Япония
Боб Дилан	2016г.	Дулут, Миннесота США
Светлана Алексиевич	2015г.	Станислав, СССР
Патрик Модиано	2014г.	Булонь-Бийанкур, Франция
Элис Энн Манро	2013г.	Вингем, Канада
Мо Янь	2012г.	Шаньдун, КНР
Тумас Транстремер	2011г.	Стокгольм, Швеция
Марио Варгас Льоса	2010г.	Арекипа, Перу
Герта Мюллер	2009г.	Ницкидорф, Румыния
Жан-Мари Гюстав Леклезио	2008г.	Ницца, Франция
Дорис Лессинг	2007г.	Керманшах, Персия
Орхан Памук	2006г.	Стамбул, Турция
Гарольд Пинтер	2005г.	Лондон, Великобритани
Эльфрида Елинек	2004г.	Мюрццушлаг, Австрия
Джон Максвелл Кутзее	2003г.	Кейптаун, ЮАР
Имре Кертес	2002г.	Будапешт, Венгрия
Видиадхар Сураджпрасад Найпол	2001г.	Тринидад, Тринидад и Тобаго
Гао Синцзянь	2000г.	Ганьчжоу, КНР
Гюнтер Грасс	1999г.	Вольный город Данциг, Германия
Жозе Сарамаго	1998г.	Азиньяга, Португалия
Дарио Фо	1997г.	Санджано, Италия
Вислава Шимборска	1996г.	Бнин, Польша
Шеймус Хини	1995г.	Кастлдоусон, Ирландия
Кэнзабуро Оэ	1994г.	Осэ, Япония
Тони Моррисон	1993г.	Лорейн, США
Дерек Уолкотт	1992г.	Кастри, Сент-Люсия
Надин Гордимер	1991г.	Гаутенг, ЮАР
Октавио Пас	1990г.	Мехико, Мексика
Камило Хосе Села	1989г.	Ирия, Испания
Нагиб Махфуз	1988г.	Каир, Египет
Иосиф Бродский	1987г.	Ленинград, СССР
Воле Шойинка	1986г.	Абеокута, Нигерия
Клод Симон	1985г.	Антананариву, Мадагаскар
Ярослав Сейферт	1984г.	Прага, Чехия
Уильям Голдинг	1983г.	Сент-Коламб Майнор, Великобритания
Габриэль Гарсия Маркес	1982г.	Аракатака, Колумбия
Элиас Канетти	1981г.	Русе, Болгария
Чеслав Милош	1980г.	Шетени, Россия
Одисеас Элитис	1979г.	Ираклион, Греция
Исаак Башевис Зингер	1978г.	Леончин, Россия
Висенте Алейксандре	1977г.	Севилья, Испания
Сол Беллоу	1976г.	Лашин, Канада
Эудженио Монтале	1975г.	Генуя, Италия
Эйвинд Йонсон	1974г.	Салтшобаден, Швеци
Харри Мартинсон	1974г.	Йемсхёг, Швеция
Патрик Виктор Мартиндейл Уайт	1973г.	Лондон, Великобритани
Генрих Белль	1972г.	Кёльн, Германия
Пабло Неруда	1971г.	Парраль, Чили
Александр Исаевич Солженицын	1970г.	Кисловодск, СССР
Сэмюэл Беккет	1969г.	Дублин, Ирландия
Ясунари Кавабата	1968г.	Осака, Япония
Мигель Астуриас	1967г.	Гватемала, Гватемала
Шмуэль Йозеф Агнон	1966г.	Бучач, Австро-Венгрия
Нелли Закс	1966г.	Шёнеберг, Германия
Михаил Александрович Шолохов	1965г.	Кружилин, СССР
Жан-Поль Сартр	1964г.	Париж, Франция
Георгос Сеферис	1963г.	Урла, Турция
Джон Стейнбек	1962г.	Салинас, США
Иво Андрич	1961г.	Долац, Австро-Венгрия
Сен-Жон Перс	1960г.	Пуэнт-а-Питр, Гваделупа
Сальваторе Квазимодо	1959г.	Модик, Итали
Борис Леонидович Пастернак	1958г.	Москва, Россия
Альбер Камю	1957г.	Мондови, Алжир
Хуан Рамон Хименес	1956г.	Андалусия, Испания
Хальдоур Кильян Лакснесс	1955г.	Рейкявик, Исландия
Эрнест Миллер Хемингуэй	1954г.	Оук-Парк, США
Уинстон Леонард Спенсер Черчилль	1953г.	Бланим-Пэлис, Великобритания
Франсуа Мориак	1952г.	Бордо, Франция
Пер Фабиан Лагерквист	1951г.	Вексьё, Швеция
Бертран Рассел	1950г.	Рейвенскрофт, Великобритания
Уильям Фолкнер	1949г.	Нью-Олбани, США
Томас Стернз Элиот	1948г.	Сент-Луис, США
Андре Жид	1947г.	Париж, Франция
Герман Гессе	1946г.	Кальв, Германия
Габриела Мистраль	1945г.	Викуньа, Чили
Йоханнес Йенсен	1944г.	Химмерланд, Дания
Франс Эмиль Силланпя	1939г.	Хямеэнкюрё, Великое княжество Финляндское (Российская империя)
Перл Бак	1938г.	Хилсборо, США
Роже Мартен Дю Гар	1937г.	Нейи-сюр-Сен, Франция
Юджин ОНил	1936г.	Нью-Йорк, США
Луиджи Пиранделло	1934г.	Джирдженти, Италия
Иван Алексеевич Бунин	1933г.	Воронеж, Россия
Джон Голсуорси	1932г.	Кингстон-Хилл, Великобриания
Эрик Карлфельдт	1931г.	Фолькерна, Швеция
Синклер Льюис	1930г.	Соук-Сентер, США
Томас Манн	1929г.	Любек, Германи
Сигрид Унсет	1928г.	Калуннборг, Дания
Анри Бергсон	1927г.	Париж, Франция
Грация Деледда	1926г.	Нуоро, Италия
Джордж Бернард Шоу	1925г.	Дублин, Ирландия
Владислав Станислав Реймонт	1924г.	Кобеле-Вельке, Российская империя
Уильям Батлер Йитс	1923г.	Дублин, Ирландия
Хасинто Бенавенте - И - Мартинес	1922г.	Мадрид, Испания
Анатоль Франс	1921г.	Париж, Франция
Кнут Гамсун	1920г.	Лом, Норвегия
Карл Фридрих Георг Шпиттелер	1919г.	Листал, Швецария
Карл Адольф Гьеллеруп	1917г.	Рохольт, Дания
Хенрик Понтоппидан	1917г.	Фредерисии, Дания
Карл Густав Вернер фон Хейденстам	1916г.	Эльсхаммар, Швеция
Ромен Роллан	1915г.	Кламси, Франция
Рабиндранат Тагор	1913г.	Калькутта, Индия
Герхардт Гауптман	1912г.	Оберзальцбрунн, Германия
Морис Метерлинк	1911г.	Гент, Бельгия
Пауль Йоханн Людвиг фон Хейзе	1910г.	Берлин, Германия
Сельма Лагерлеф	1909г.	Вермланд, Швеция
Рудольф Кристоф Эйкен	1908г.	Аурих, Германия
Джозеф Редьярд Киплинг	1907г.	Бомбей, Индия
Джозуэ Кардуччи	1906г.	Валь-ди-Кастелло, Итали
Генрик Сенкевич	1905г.	Окжейска, Российская империя
Фредерик Мистраль	1904г.	Мейан, Франция
Хосе Мария Вальдо Эчегарай - И - Эйсагирре	1904г.	Мадрид, Испания
Бьернстерне Мартиниус Бьернсон	1903г.	Квикне, Норвегия
Теодор Моммзен	1902г.	Гардинг, Дания
Рене Сюлли-Прюдом	1901г.	Париж, Франция
"""


def extract_name_year(data):
    lines = data.strip().split("\n")
    authors = {}
    for line in lines:
        match = re.match(r"(.+)\s+(\d{4}г\.)\s+.+", line)
        if match:
            name, year = match.groups()
            authors[name.strip()] = year.strip()[:-2]
    return authors


print(extract_name_year(data).get(input()))
