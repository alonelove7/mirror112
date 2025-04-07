#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🔵 لینک گروه'
    ST_BN1_URL = 'https://t.me/kingleech'
    ST_BN2_NAME = 'لینک کانال 🔵'
    ST_BN2_URL = 'https://t.me/king_network7'
    ST_MSG = '''〽️ توسط ربات کینگ لیچ قادر خوهید بود لینک های تورنت و یوتیوب ، فایل و... را با سرعت بالا و بدون محدودیت دانلود کنید\n\n❓قبل از استفاده از ربات راهنما را با ارسال دستور {help_command} مطالعه کنید\n\n🆔@King_Network7'''
    ST_BOTPM = '''❔ ربات فایل و لینک های مربوط به شما را اینجا ارسال میکند\n\n🆔@King_Network7'''
    ST_UNAUTH = '''⭕️ حساب شما داخل ربات هنوز مجاز نیست ⭕️'''
    OWN_TOKEN_GENERATE = '''⭕️ این توکن موقت متعلق به شما نیست\n⭕️ برای استفاده توکن خود را ایجاد کنید\n\n🆔@King_Network7'''
    USED_TOKEN = '''⭕️ این توکن قبلا منقضی شده است\n⭕️ مجددا توکن جدیدی ایجاد نمایید\n\n🆔@King_Network7'''
    LOGGED_PASSWORD = '''⭕️ ربات قبلا از طرق پسورد لاگین شده است نیازی به پذیرش توکن نیست ⭕️'''
    ACTIVATE_BUTTON = '🌀 فعالسازی توکن 🌀'
    TOKEN_MSG = '''🔰 توکن شما لا موفقیت ایجاد شد\n🈳 توکن: <code>{token}</code>\n🗓 اعتبار: {validity}\n\n🆔@King_Network7'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '❇️ فعالسازی موفقیت آمیز بود ❇️'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '⚙️ قبلا در ربات لاگین کرده اید ⚙️'
    INVALID_PASS = '⭕️ پسورد نامعتبر است\n⭕️ پسورد صحیح را ارسال کنید\n\n🆔@King_Network7'
    PASS_LOGGED = '✅ لاگین در ربات موفقیت آمیز بود ✅'
    LOGIN_USED = '❔ نحوه لاگین در ربات\n©️ <code>/cmd [password]</code>\n\n🆔@King_Network7'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '🧾 نمایش لاگ های ربات 🧾'
    WEB_PASTE_BT = '📨 Web Paste 📨'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '🔺 پایه 🔺'
    USER_BT = '🔺 کاربران 🔺'
    MICS_BT = '🔻 Mics 🔻'
    O_S_BT = '🔻 ادمین ها 🔻'
    CLOSE_BT = '🔸 بستن 🔸'
    HELP_HEADER = "❓ منوی راهنما ربات کینگ لیچ\n❗️ برای دیدن جزییات روی دستورات کلیک کنید\n\n🆔@King_Network7"

    # async def stats(client, message):
    BOT_STATS = '''📊 وضعیت ربات کینگ لیچ:
🎛 آپتایم: {bot_uptime}

🔘 حافظه رام:
➖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

🔘 حافظه Swap:
➖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

🔘 دیسک:
➖ b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}

🆔@King_Network7'''

    SYS_STATS = '''📊 وضعیت سیستم عامل:
©️ آپتایم: <code>{os_uptime}</code>
©️ ورژن: <code>{os_version}</code>
©️ آرچ: <code>{os_arch}</code>

📊 وضعیت شبکه: 
®️ دانلود: <code>{up_data}</code>
®️ آپلود: <code>{dl_data}</code>
®️ پکت ارسالی: <code>{pkt_sent}k </code>
®️ پکت دریافتی: <code>{pkt_recv}k </code>
®️ کل داده های ورودی/خروجی: <code>{tl_data}</code>

📊 وضعیت پردازنده:
®️ چک: <code>{cpu_bar} {cpu}% </code>
®️ فرکانس: <code>{cpu_freq}</code>
®️ میانگین بار: <code>{sys_load}</code>
®️ تعداد هسته: <code>{total_core}</code>
®️ پردازنده قابل استفاده: <code>{cpu_use}</code>

🆔@King_Network7'''
    REPO_STATS = '''📊 وضعیت سورس ربات:
➖ ورژن فعلی: <code>{bot_version}</code>
➖ آخرین ورژن: <code>{lat_version}</code>
➖ آخرین تغییرات: <code>{commit_details}</code>

🆔@King_Network7'''
    BOT_LIMITS = '''📕 محدودیت های ربات:
🀄️ محدودیت مستقیم: <code>{DL}GB </code>
🀄️ محدودیت تورنت: <code>{TL}GB </code>
🀄️ محدودیت درایو: <code>{GL}GB </code>
🀄️ محدودیت یوتیوب: <code>{YL}GB </code>
🀄️ محدودیت پلی لیست: <code>{PL} </code>
🀄️ محدودیت مگا: <code>{ML}GB </code>
🀄️ محدودیت کلون: <code>{CL}GB </code>
🀄️ محدودیت لیچ: <code>{LL}GB </code>
🀄️ محدودیت زمانی کاربر: <code>{UTI} </code>
🀄️ محدودیت تسک کاربر: <code>{UT} </code>
🀄️ محدودیت تسک ربات: <code>{BT} </code>
🀄️ اعتبار توکن: <code>{TV} </code>

🆔@King_Network7'''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '♻️ درحال راه اندازی مجدد ♻️'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''✅ راه اندازی مجدد موفقیت آمیز بود
📅 تاریخ: <code>{time}</code>
⏰ زمان: <code>{date}</code>

🆔@King_Network7'''
    RESTARTED = '''✅ راه اندازی مجدد انجام شد ✅'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '🕹 درحال برسی پینگ...\n\n🆔@King_Network7'
    PING_VALUE = '🖲 پینگ ربات: <code>{value}ms</code>\n\n🆔@King_Network7'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """♻️ تسک جدیدی استارت شد
⚙️ حالت: {Mode}
👤 کاربر: {Tag}"""
    LINKS_SOURCE = """📦 منبع: 
➡️ <code>{Source}</code>

🆔@King_Network7"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "☯️ تسک استارت شد وضعیت داخل گروه قابل مشاهده است\n🌐 لینک ارسالی توسط شما: <a href='{msg_link}'>کلیک کنید</a>\n\n🆔@King_Network7"
    L_LOG_START =           "📳 لیچ جدیدی استارت شد\n👤 کاربر: {mention} ( #ID{uid} )\n🌐 منبع: <a href='{msg_link}'>کلیک کنید</a>\n\n🆔@King_Network7"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '{Name}\n'
    SIZE =                  '🔸 حجم: <code>{Size}</code> \n'
    ELAPSE =                '🔸 زمان سپری شده: <code>{Time}</code> \n'
    MODE =                  '🔸 حالت: <code>{Mode}</code> \n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '🔸 تعداد فایل ها: <code>{Files}</code> \n'
    L_CORRUPTED_FILES =     '🔸 فایل های خراب: <code>{Corrupt}</code> \n'
    L_CC =                  '🔸 توسط کاربر: <code>{Tag}</code> \n'
    PM_BOT_MSG =            ''
    L_BOT_MSG =             '✅ ارسال شد'
    L_LL_MSG =              '✅ ارسال شد\n'
    
    # ----- MIRROR -------
    M_TYPE =                '🔸 نوع: <code>{Mimetype}</code> \n'
    M_SUBFOLD =             '🔸 زیرپوشه ها: <code>{Folder}</code> \n'
    TOTAL_FILES =           '🔸 فایل ها: <code>{Files}</code> \n'
    RCPATH =                '🔸 مسیر: <code>{RCpath}</code> \n'
    M_CC =                  '🔸 توسط: <code>{Tag}</code> \n\n'
    M_BOT_MSG =             '✅ ارسال شد'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ لینک کلود'
    SAVE_MSG =        '💾 ذخیره 💾'
    RCLONE_LINK =     '♻️ لینک'
    DDL_LINK =        '📎 {Serv} لینک'
    SOURCE_URL =      '🔐 منبع'
    INDEX_LINK_F =    '🗂 لینک مستقیم'
    INDEX_LINK_D =    '⚡ لینک مستقیم'
    VIEW_LINK =       '🌐 مشاهده'
    CHECK_PM =        '📥 مشاهده'
    CHECK_LL =        '🖇 مشاهده'
    MEDIAINFO_LINK =  '📋 مدیا اینفو'
    SCREENSHOTS =     '🩻 اسکرین شات'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '◾️ وضعیت/نام: <code>{Name}</code>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n🔺 {Bar}'
    PROCESSED =         '\n◽️ دانلود: <code>{Processed}</code>'
    STATUS =            '\n◾️ مرحله تسک: <a href="{Url}">{Status}</a>'
    ETA =               '\n◽️ زمان اتمام: <code>{Eta}</code>'
    SPEED =             '\n◾️ سرعت: <code>{Speed}</code>'
    ELAPSED =           '\n◽️ زمان سپری شده: <code>{Elapsed}</code>'
    ENGINE =            '\n◾️ منبع: <code>{Engine}</code>'
    STA_MODE =          '\n◽️ حالت : <code>{Mode}</code>'
    SEEDERS =           '\n◾️سیدرز: <code>{Seeders}</code>'
    LEECHERS =          '\n◽️ لیچر: <code>{Leechers}</code>'

    ####--------SEEDING----------
    SEED_SIZE =      '\n◾️ حجم: <code>{Size}</code>'
    SEED_SPEED =     '\n◽️ سرعت: <code>{Speed}</code>'
    UPLOADED =       '\n◾️ آپلود: <code>{Upload}</code>'
    RATIO =          '\n'
    TIME =           '\n◽️ زمان: <code>{Time}</code>'
    SEED_ENGINE =    '\n◾️ منبع: <code>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n◾️ حجم: <code>{Size}</code>'
    NON_ENGINE =     '\n◽️ منبع: <code>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =           '\n👤 کاربر: <code>{User}</code> | '
    ID =             '🌀 آیدی: <code>{Id}</code>'
    BTSEL =          '\n◾️ انتخاب: <code>{Btsel}</code>'
    CANCEL =         '\n\n❌ {Cancel}\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n'

    ####------FOOTER--------
    FOOTER = '📊 وضعیت ربات\n'
    TASKS =  '♦️ تسک ها: {Tasks}\n'
    BOT_TASKS = '♦️ تسک ها: {Tasks}/{Ttask}\n'
    Cpu = '🖱 <b>CPU</b>: <code>{cpu}%</code> | '
    FREE =                      '<b>F:</b> <code>{free} [{free_p}%]</code>'
    Ram = '\n🖱 <b>RAM</b>: <code>{ram}%</code> | '
    uptime =                     '\n🖱 <b>UPTIME</b>: <code>{uptime}</code>'
    DL = '\n🖱 <b>DL</b>: <code>{DL}/s</code> | '
    UL =                        '🖱 <b>UL</b>: <code>{UL}/s</code>\n\n🆔@King_Network7'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = 'صفحه\n{Page}'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '⚜️ این فایل یا فولدر در آرشیو ربات موجود می باشد\n🛜 برای مشاهده {content} کلیک کنید\n\n🆔@King_Network7'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '🔢 شمارش: <code>{LINK}</code>'
    COUNT_NAME = '*️⃣ نام: <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '*️⃣ حجم: <code>{COUNT_SIZE}</code>\n'
    COUNT_TYPE = '*️⃣ نوع: <code>{COUNT_TYPE}</code>\n'
    COUNT_SUB =  '*️⃣ فولدر ها: <code>{COUNT_SUB}</code>\n'
    COUNT_FILE = '*️⃣ فایل ها: <code>{COUNT_FILE}</code>\n'
    COUNT_CC =   '👤 کاربر: <code>{COUNT_CC}</code>\n\n🆔@King_Network7'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '🔍 درحال جستجو برای "{NAME}"\n\n🆔@King_Network7'
    LIST_FOUND = '📮 {NO} مورد نتیجه برای "{NAME}" یافت شد\n\n🆔@King_Network7'
    LIST_NOT_FOUND = '⭕️ جستجو برای "{NAME}" نتیجه ای نداشت\n\n🆔@King_Network7'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''⭕️ تسک فعالی در ربات وجود ندارد
    
➖➖➖➖➖➖➖➖➖➖➖➖
🖱 <b>CPU</b>: <code>{cpu}%</code> | <b>F:</b> <code>{free} [{free_p}%]</code>
🖱 <b>RAM</b>: <code>{ram}%</code> | 🖱 <b>UPTIME</b>: <code>{uptime}</code>

🆔@King_Network7'''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''⚙️ تنظیمات کاربر:
🪪 نام: <code>{NAME}</code> (<code>{ID}</code>)
☎️ آی دی: <code>{USERNAME}</code> 
🔩 تلگرام DC: <code>{DC}</code> 
🇮🇷 زبان: <code>{LANG}</code> 

🆔@King_Network7'''

    UNIVERSAL = '''⚙️ تنظیمات کلی:
🪪 نام: <code>{NAME}</code>
🟧 گزینه های YT-DLP: <code>{YT}</code>
🟧 تسک روزانه: <code>{DT}</code> 
🟧 آخرین استفاده: <code>{LAST_USED}</code> 
🟧 مدیا اینفو: <code>{MEDIAINFO}</code> 
🟧 حالت ذخیره: <code>{SAVE_MODE}</code> 
🟧 یوزر بات: <code>{BOT_PM}</code> 

🆔@King_Network7'''

    MIRROR = '''⚙️ تنظیمات میرور/کلون:
🪪 نام: <code>{NAME}</code>
🟪 کانفیگ کلون: <code>{RCLONE}</code>
🟪 پیشوند میرور: <code>{MPREFIX}</code> 
🟪 پسوند میرور: <code>{MSUFFIX}</code> 
🟪 تغییرنام میرور: <code>{MREMNAME}</code> 
🟪 میرور روزانه: <code>{DM}</code> 
🟪 سرور DDL: <code>{DDL_SERVER}</code> 
🟪 حالت TD کاربر: <code>{TMODE}</code> 
🟪 کل کاربران TD: <code>{USERTD}</code> 

🆔@King_Network7'''

    LEECH = '''⚙️ تنظیمات لیچ برای <code>{NAME}</code>:
🟦 لیچ روزانه: <code>{DL}</code>
🟦 نوع لیچ: <code>{LTYPE}</code> 
🟦 کپشن لیچ: <code>{LCAPTION}</code> 
🟦 پیشوند لیچ: <code>{LPREFIX}</code> 
🟦 پسوند لیچ: <code>{LSUFFIX}</code> 
🟦 دامپ لیچ: <code>{LDUMP}</code> 
🟦 تغییرنام لیچ: <code>{LREMNAME}</code> 
🟦 تامبنیل کاستوم: <code>{THUMB}</code> 
🟦 حجم تقسیم لیچ: <code>{SPLIT_SIZE}</code> 
🟦 تقسیم های مساوی: <code>{EQUAL_SPLIT}</code> 
🟦 مدیاگروپ: <code>{MEDIA_GROUP}</code> 

🆔@King_Network7'''
