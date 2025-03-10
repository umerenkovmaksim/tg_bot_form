# БОТ --------------------------
# токен бота
TOKEN = '7836783041:AAFtLuQazBhqUs78zrjek9CB2W5TE8vmmOI'
# канал админов
ADMIN_CHANNEL_ID = '@test_python_channel2'
# время паузы перед одобрением анкеты (в секундах)
MESSAGE_DELAY = 2

# СООБЩЕНИЯ --------------------
# приветственное сообщение (кнопка /start)
HELLO_MESSAGE = "Добро пожаловать! Этот бот помогает пройти первичный этап отбора на вакансию «Специалист технической поддержки (удаленно)».\n\nНажмите «Начать», чтобы заполнить анкету или узнать больше о вакансии."
# информация о работе (информация о работе)
WORK_INFO = f"Сотрудник удаленной поддержки клиентов (письменно)\n\nЭто возможность присоединиться к крупнейшей IT компании и начать работать в комфортных условиях из дома.\n\nМы ищем ответственных и целеустремленных кандидатов, которые готовы отвечать на письма пользователей и решать их проблемы.\n\nОбязанности: — Удаленно, консультирование и ответы на вопросы/претензии клиентов компании.\n\nГрафик работы индивидуальный, подстраивается под вас! Можно работать от 20 до 48 часов в неделю и совмещать с учебой/другой работой.\n\nСкорее заполняй анкету и начинай зарабатывать вместе с нами!"
# сообщение после отправки анкеты
END_FORM = "Спасибо! Ваша анкета отправлена. В ближайшее время вы получите предварительный ответ по вашей кандидатуре."
# уведомление о программе "Приведи друга"
REFERRAL_NOTIFICATION = 'Прошу вас не игнорировать оформление карты. К моменту трудоустройства вам необходимо будет получить и активировать зарплатную карту.\n\nТакже напоминаем о нашей программе «Приведи друга». Участие в программе позволяет вам и приглашенному другу получить по 30 000 рублей. Условие — успешное прохождение отбора и работа друга в течение минимум 3 недель.\n\nДля участия просто поделитесь вашей уникальной ссылкой. Все кандидаты, которые придут по вашей ссылке, будут закреплены за вами, а бонусы будут автоматически начислены.'
# сообщение после паузы (подтверждение работы)
WORK_QUESTION = 'Благодарим вас за ожидание!\n\nПоздравляем, вы успешно прошли предварительный отбор!\n\nВаши индивидуальные условия:\n- работа онлайн через нашу CRM-систему, ответы на сообщения пользователей (письменно) по заданному скрипту;\n- график работы вы составляете индивидуально, от 20 до 48 часов в неделю;\n- оплата еженедельно, ставка на старте работы 320 рублей/час;\n\nДля продолжения подтвердите, актуальна ли для вас данная вакансия и сможете ли вы приступить к работе в ближайшие 30 дней.'
# оформление карты
CONFIRM_WORK = "Отлично! Чтобы продолжить, вам необходимо оформить бесплатную дебетовую карту, на которую будет переводиться ваша заработная плата.\n\nДля данной вакансии предусмотрена еженедельная оплата, исходя из отработанных часов, по ставке 320 рублей/час. Учитывается время нахождения в сети, в течение которого к вам могут обратиться за помощью (даже если никто не напишет)."
# сообщение для приглашения рефералов
REFERRAL_SHARE = "Давай работать и зарабатывать вместе! Вакансия: «Сотрудник техподдержки письменно (удаленно)». Присоединяйся!"
# сообщение после приглашения рефералов
AFTER_REFERRAL_MESSAGE = "Спасибо! Ваша анкета отправлена. Мы свяжемся с вами после активации зарплатной карты для выдачи обучающего материала и введения в курс работы.\n\nПожалуйста при оформлении карты нажмите соответствующую кнопку, чтобы ускорить процесс проверки!*"
# последнее сообщение (после оформления карты)
CARD_END_MESSAGE = "Спасибо, напоминаем что для продолжения вам нужно оформить, получить и активировать карту.\n\nДля активации нужно совершить любую транзакцию по карте.\n\nЕсли вы выполнили условия то ожидайте, в случае положительного решения с вами вяжется менеджер в ближайшее время.\n\n"
# ссылка на создание карты
CARD_CREATE_URL = "https://tplto.com/go/803017f7cb10426bf9bee4242aaa9b3e365b64d1eb0a0b0b/?erid=2Vtzqw6bEL6"

# ЗАПОЛЕНЕНИЕ АНКЕТЫ -----------
# вопрос о имени и фамилии
NAME_AND_SURNAME = "Пожалуйста, укажите ваше имя и фамилию."
# вопрос о контактных данных
CONTACT = "Укажите ваш номер телефона или email для связи."
# вопрос о возрасте
AGE = "Укажите, пожалуйста, сколько вам полных лет на момент заполнения анкеты."
# вопрос о типе работы
WORK_TYPE = "Вы рассматриваете вакансию как основную работу или как подработку?"
# вопрос о городе проживания
CITY = "Напишите город вашего проживания."
