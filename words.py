import utils
dict= {
    "UZ": {
        "search_inline_mode": "🔎 Qidirish",
        "confirm_menu": ("✅ Yuborish", "🚫  Bekor qilish"),
        "not_know": "❗ Buyruqni tushunmadim! ",
        "sign up": {
            "lan": "Ismingizni kiriting.",
            "name": "Siz haqingizda adminga xabar berdim. Hisobingiz tasdiqlanishini kuting.",
            "user_status_change_to_member_user_message": "✅ Hisobingiz tasdiqlandi!",
            "user_status_change_to_member_admin_message": "✅ Foydalanuvchi hisobi tasdiqlandi!",
            "user_status_change_to_none_user_message": "❗ Hisobingizni bloklandi!",
            "user_status_change_to_none_admin_message": "❗ Foydalanuvchi hisobi bloklandi!",
            "bug": "❗ Foydalanuvchiga xabar yuborishda qandaydir muammo bo'ldi. Men uni bazadan tozalab yubordim. Ehtimol, u botni bloklagan bo'lishi mumkin.",
            "old_messsage": "❗ Ushbu xabar eski va foydalanuvchi allqachon bazzadan o'chirib yuborilgan!"
            },
        "block_user": "❗ Sizning hisobingiz tasdiqlanmagan!",
        "start": {
            "admin": "Assalomu alaykum, admin!",
            "user": "Assalomu alaykum"
        },
        "main_menu": {
            "text": "🏠 Asosiy menyu",
            "menu": ("📦 Mahsulotlar", "🛒 Savat", "📬 Mening buyurtmalarim", "📒 Hisobotlar", "📂 Qosimsha narsalar", "⚙️ Sozlamalar")
        },
        "additional_items": {
            "main_text": "Kerakli menyuni tanlang.",
            "menu": ("⚖️ Balans", "💲USD kursi", "🧾 Narxlar ro'yhati", "🏠 Asosiy menyu"),
            "dollar_kursi": lambda kurs_rate, date: f"<b>VALYUTA KURSI:</b>\n\n1 USD - {kurs_rate} USD\n\n<b>O'zbekiston Respublikasi Markaziya banki - {date}</b>",
            "balans": lambda balans: f"<b>Hisobingiz:</b>\n\n{balans} USD"
        },
        "confirm_order": {
            "in_text": "Buyurtma raqamini kiriting.",
            "confirm_menu": ("✅ Tasdiqlash", "❌ Bekor qilish"),
            "not_found_user": "Foydalanuvchi topilmadi!",
            "not_found_product": "Mahsulot topilmadi!",
            "not_found_order": "Buyurtma topilmadi!",
            "confirm_text": "✅ Buyurtma tasdiqlandi!",
            "rejected_text": "❌ Buyurtma rad etildi!",
            "not_found_order": "❗ Buyurtma topilmadi!",
            "order_data": lambda name, size, soni, order_price, product_price, status: f"<b>Buyurtma ma'lumotlari:</b>\n\n<b>Mahsulot nomi:</b> {name}\n<b>Mahsulot o'lchami:</b> {size}\n<b>Buyurtma soni:</b> {soni}\n<b>Mahsulot narxi:</b> {product_price} USD\n<b>Buyurtma narxi:</b> {order_price} USD\n<b>Holati:</b> {status}",
            "alert_order_user": lambda order_id, status: f"❗ Sizning {order_id} raqamli buyurtmangiz {'tasdiqlandi!' if status == 'confirmed' else 'rad etildi!'}"
        },
        "settings": {
            "main_text": "Nimani sozlamoqchisiz?",
            "main_menu": ("Tilni sozlash", "🏠 Asosiy menyu"),
            "admin_menu": ("Tilni sozlash", "Qarzdorlik bildirishnomasi vaqtini sozlash", "Qarzdorlik limitini sozlash", "🏠 Asosiy menyu"),
            "set_lan_text": "Tilni tanlang.",
            "changed_lan_text": "Til o'zbek tiliga o'zgartirildi!",
            "change_time_text": lambda soat, minut: f"Joriy tanlangan vaqt {soat}:{minut}",
            "change_limit_text": lambda limit: f"Hozirgi limit: {limit} USD\n\nYangi limitni yuboring."
        },
        "debtor_message": lambda name, balans : f"❗ {name} siz qarzdorsiz!\n\nHisobingiz: {utils.pulni_qismlash(balans)} USD",
        "my_orders": {
            "main_menu": ("🆕 Yangi", "❌ Rad etilgan", "🕙 Tasdiqlanmagan", "🏠 Asosiy menyu"),
            "main_text": "Qaysi holatdagi buyurtmalaringiz ro'yhatini olmoqchisiz?",
            "not_new_order": "❗ Oxirgi 1 haftada buyurtma berilmagan!",
            "not_canceled_orders": "❗ Bekor qilingan buyurtmalar topilmadi!",
            "not_pending_orders": "❗ Tasdiqlanishi kutilayotgan buyurtmalar topilmadi!",
            "my_orders_table_columns": ("user_ID", "Ism-familya", "Buyurtma raqami", "Mahsulot nomi", "Mahsulot o'lchami", "Buyurtmalar soni", "Buyurtma narxi", "Buyurtma vaqti", "Buyurtma holati"),

        },
        "manage_users": {
            "main_text": "Foydalanuvchilarni boshqarish menyusidasiz!",
            "main_menu": ("Foydalanuvchilar ro'yhati", "Xabar yuborish", "🏠 Asosiy menyu"),
            "input_message_text": "Xabarni yuboring.",
            "users_list_text": "Foydalanuvchini tanlang.",
            "not_found_user": "❗ Foydalanuvchi topilmadi!",
            "manage_user_text": "Buyuruqni tanlang.",
            "acc_message": "✅ Xabar qabul qilindi!",
            "mission_acc": "✅ Vazifa bajarildi!",
            "acc_alerts_for_user": {
                "del": "Siz bazadan o'chirildingiz!",
                "block": "Siz bloklandingiz!",
                "active": "Sizning hisobingiz faollashtirildi!",
                "addadmin": "Siz admin qilindingiz!",
                "rmAdmin": "Siz adminlikdan olindingiz!"
            },
            "thisIsAdmin": "Bu foydalanuvchi oldin admin qilingan!",
            "thisIsNotAdmin": "Bu foydalanuvchi admin qilinmagan!",
            "user_data": lambda name, id, balans, status: f"Foydalanuvchi ma'lumotlari:\n\nIsm-familya: {name}\nID: {id}\nBalans: {utils.pulni_qismlash(balans)} USD\nHolati: {status if status else 'block'}",
            "manage_user_menu": ("Bazadan o'chirish", "Bloklash", "Faollashtirish", "Admin qilish", "Adminlikdan olish", "Balansni to'ldirish", "⬅ Ro'yhatga qaytish"),
            "send_summa": "Qancha pul qo'shamiz?"
        },
        "admin_menu": ("Buyurtmani ko'rish", "Hisobotlar", "Mahsulotlar", "Foydalanuvchilar", "⚙️ Sozlamalar"),
        "reports": {
            "main_text": "Qaysi turdagi hisobotni olmoqchisiz?",
            "main_menu": ("Kunlik", "Haftalik", "Oylik", "Yillik", "🏠 Asosiy menyu"),
            "admin_menu": ("Kunlik", "Haftalik", "Oylik", "Yillik", "❌ Rad etilgan", "🕙 Tasdiqlanmagan", "Tovarlar", "🏠 Asosiy menyu"),
            "not_report": "Hisobot tayyorlash uchun buyurtma mavjud emas!",
            "alert": "Menyulardan birini tanlang."
        },
        "manage_products":{
            "main_text": "Siz mahsulotlarni boshqarish bo'limidasiz!",
            "main_menus": ("Mahsulot qo'shish", "Mahsulot o'chirish", "Mahsulot miqdorini o'zgartirish", "🏠 Asosiy menyu")
        },
        "change_count_product": {
            "input_text": "Mahsulotni idsini kiriting.",
            "count_input_text": "Mahsulotning yangi miqdorini kiriting.",
            "changed_count_product": "✅ Mahsulot miqdori yangilandi!",
            "enter_an_integer": "Butun son kiriting.",
            "not_find_product": "❗ Bunday mahsulot topilmadi!"
        },
        "del_product": {
            "input_text": "Mahsulotni idsini kiriting.",
            "deleted_product": "❗ Mahsulot o'chirildi!",
            "not_find_product": "❗ Bunday mahsulot topilmadi!"
        },
        "changed_count_product_message": lambda name, size: f"{name} mahsuloti {size} o'lchami miqdori yangilandi!",  
        "changed_count_order_message": lambda order_id, user_name: f"❗ {user_name} {order_id} raqamli buyurtmasi sonini yangiladi",  
        "deleted_product_message": lambda name, size: f"{name} mahsuloti {size} o'lchami bazadan o'chirildi!",
        "deleted_order_message": lambda order_id, user_name: f"❗ {user_name} {order_id} raqamli buyurtmasini bekor qildi!",
        "new_product_message": lambda name: f"🆕 <b>Bazaga yangi mahsulot qo'shildi!\nNomi:</b> {name}",
        "sending_message_users_count": lambda sending_users : f"✅ {sending_users} ta foydalanuvchiga xabar yuborildi!",
        "basket": {
            "order_manage_menu": ("🔢 Miqdorini o'zgartirish", "❌ Buyurtmani bekor qilish"),
            "order_data": lambda name, size, soni, price, date, order_id: (
                f"<b>{order_id} raqamli buyurtma ma'lumotlari:</b>\n\n"
                f"<b>Nomi:</b> {name}\n"
                f"<b>O'lchami:</b> {size}\n"
                f"<b>Soni:</b> {soni}\n"
                f"<b>Narxi:</b> {utils.pulni_qismlash(price)} USD\n"
                f"<b>Buyurtma berilgan sana:</b> {date.split()[0]}"
                ),

            "not_found_order": "❗ Bu nomdagi mahsulotga buyurtma topilmadi!",
            "empty_basket": "🛒 Savat bo'sh",
            "send_order_count": "Buyurtmalar sonini nechtaga o'zgartirmoqchisiz!",
            "changed_order_count": "✅ Buyurtmalar soni o'zgartirildi!",
            "deleted_order": "❗ Buyurtma o'chirildi!",
            "error_order_count": "❗ Buyurtmalar soni noto'g'ri kiritilgan. Qayta urinib ko'ring.",
            "save_order": lambda balans: f"Buyurtmangiz ma'lumotlari yangilandi!\n Hisobingiz: {utils.pulni_qismlash(balans)} USD",
        },
        "add_product": {
            "send_name": "Mahsulot nomini kiriting.",
            "saved_name": "Mahsulot nomi saqlandi!",
            "send_size": "Mahsulot o'lchamini kiriting.",
            "save_not_size": "ushbu nomdagi va o'lchamdagi mahsulot bazada mavjud!",
            "saved_size": "Mahsulot o'lchami saqlandi!",
            "send_soni": "Mahsulot sonini kiriting.",
            "send_digit": "Menga son yuboring.",
            "saved_soni": "Mahsulotlar soni saqlandi!",
            "send_price": "Mahsulot narxini kiriting.",
            "saved_price": "Mahsulot narxi qabul qilindi!",
            "send_img1": "Mahsulotning 1-rasmini yuboring yoki joriy ma'lumotlarni saqlaysizmi?",
            "send_imges_menu": ("✅ Yuborish", "🚫  Bekor qilish"),
            "saved_img": "Rasm saqlandi, yana rasm yuborasizmi?",
            "product_data": lambda name, size, soni, price: (
                f"<b>Nomi:</b> {name}\n"
                f"<b>O'lchami:</b> {size}\n"
                f"<b>Soni:</b> {soni}\n"
                f"<b>Narxi:</b> {utils.pulni_qismlash(price)} USD\n"),
            "confirm_text": "Ma'lumotlarni tasdiqlaysizmi?",
            "confirm_data_menu": ("✅ Tasdiqlash", "🚫 Bekor qilish"),
            "saved_product": lambda id: f"<b>✅ Mahsulot saqlandi!</b>\n\n<b>ID:</b> {id}"
        },
        "products_user": {
            "main_menu_text": "📦 Mahsulotlar bo'limidasiz! Mahsulotni tanlang.",
             "product_data": lambda name, size, soni, price: (
                f"Mahsulot ma'lumotlari:\n\n"
                f"<b>Nomi:</b> {name}\n"
                f"<b>O'lchami:</b> {size}\n"
                f"<b>Soni:</b> {soni}\n"
                f"<b>Narxi:</b> {utils.pulni_qismlash(price)} USD\n"),
            "not_found_product": "❗ Bu nomdagi mahsulot mavjud emas!",
            "add_order_menu": "savatga qo'shish",
            "send_order_soni": "Mahsulotdan nechta harid qilmoqchisiz?",
            "save_order": lambda balans: f"Buyurtmangiz savatga tashlandi!\n Hisobingizda {utils.pulni_qismlash(balans)} USD",
            "new_order": lambda order_id: f"<b>Yangi buyurtma:</b> ID {order_id}",
            "error_order_count": "❗ Buyurtmalar soni noto'g'ri kiritilgan. Qayta urinib ko'ring."
        }},
    "RU": {
        "search_inline_mode": "🔎 поиск",
        "confirm_menu": ("✅ Отправить", "🚫 Отмена"),
        "not_know": "❗ Я не понял команду! ",
        "sign up": {
            "lan": "введите ваше имя.",
            "name": "Я сообщил о вас администратору. Подождите, пока ваша учетная запись будет подтверждена.",
            "user_status_change_to_member_user_message": "✅ Ваш аккаунт подтвержден!",
            "user_status_change_to_member_admin_message": "✅ Аккаунт обмена подтвержден!",
            "user_status_change_to_none_user_message": "❗️Ваш аккаунт заблокирован!",
            "user_status_change_to_none_admin_message": "❗️Аккаунт заблокирован!",
            "bug": "❗️ Возникла проблема с отправкой сообщения пользователю. Я удалил его из базы. Возможно, это заблокировало бота.",
            "old_message": "❗️Это сообщение старое и пользователь уже удален из базы!"
            },
        "block_user": "❗ Ваша учетная запись не подтверждена!",
        "start": {
            "admin": "Привет админ!",
            "user": "Привет"
        },
        "main_menu": {
            "text": "🏠 Главное меню",
            "menu":  ("📦 Товары", "🛒 Корзина", "📬 Мои заказы",   "📒 Отчеты", "📂 Аксессуары", "⚙️ Настройки")
        },
        "additional_items": {
            "main_text": "Выберите нужное меню.",
            "menu": ("⚖️ Баланс", "💲Курс доллара США", "🧾 прайс-лист", "🏠 Главное меню"),
            "dollar_kursi": lambda kurs_rate, date: f"<b>КУРС ВАЛЮТЫ:</b>\n\n1 USD - {kurs_rate} USD\n\n<b>Центральный банк Республики Узбекистан - {date}</b>",
            "balans": lambda balans: f"<b>Ваш счет:</b>\n\n{balans} USD"
        },
        "settings": {
            "main_text": "Что вы хотите настроить?",
            "main_menu": ("Языковые настройки", "🏠 Главное меню"),
            "admin_menu": ("Языковые настройки", "Настройка времени уведомления о задолженности", "Установка лимита долга", "🏠 Главное меню"),
            "set_lan_text": "Выберите язык.",
            "changed_lan_text": "Язык изменен на русский!",
            "change_time_text": lambda soat, minut: f"Текущее выбранное время {soat}:{minut}",
            "change_limit_text": lambda limit: f"Текущий лимит: {limit} USD.\n\nОтправьте новый лимит."
       },
        "my_orders": {
            "main_menu": ("🆕 Новое", "❌ Отклонено", "🕙 Неподтверждено", "🏠 Главное меню"),
            "main_text": "В каком статусе вы хотели бы получать список ваших заказов?",
            "not_new_order": "❗ За последнюю неделю заказов не было!",
            "not_canceled_orders": "❗ Отмененных заказов не обнаружено!",
            "not_pending_orders": "❗ Заказов, ожидающих одобрения, не найдено!",
            "my_orders_table_columns": ("user_ID", "Имя", "Номер заказа", "Наименование товара", "Размер товара", "Количество заказов", "Стоимость заказа", "Время заказа", "Статус заказа"),

        },
        "manage_users": {
            "main_text": "Вы находитесь в меню управления пользователями!",
            "main_menu": ("Список пользователей", "Отправить сообщение", "🏠 Главное меню"),
            "input_message_text": "Xabarni yuboring.",
            "users_list_text": "Выберите пользователя.",
            "not_found_user": "❗ Пользователь не найден!",
            "manage_user_text": "Выберите команду.",
            "acc_message": "✅ Сообщение доставлено!",
            "mission_acc": "✅ Миссия выполнена!",
            "acc_alerts_for_user": {
                "del": "Вас удалили из базы!",
                "block": "Вы заблокированы!",
                "active": "Ваш аккаунт активирован!",
                "addadmin": "Вы были администратором!",
                "rmAdmin": "Вас удалили из администратора!"
            },
            "thisIsAdmin": "Этот пользователь раньше был администратором!",
            "thisIsNotAdmin": "Этот пользователь не является администратором!",
            "user_data": lambda name, id, balans, status: f"информация о пользователе:\n\nИмя-фамилия: {name}\nID: {id}\nBalans: {utils.pulni_qismlash(balans)} USD\nStatus: {status if status else 'block'}",
            "manage_user_menu": ("Удалить из базы данных", "Блокировка", "Активация", "Админ", "Получить от админа", "Пополнение баланса", "⬅ Вернуться к списку"),
            "send_summa": "Сколько мы добавляем?"
        },
        "admin_menu": ("Посмотреть заказ", "Отчеты", "Продукты", "Пользователи", "⚙️ Настройки"),
        "confirm_order": {
            "in_text": "Введите номер заказа.",
            "confirm_menu": ("✅ Подтверждение", "❌ Отмена"),
            "not_found_user": "Пользователь не найден!",
            "not_found_product": "Товар не найден!",
            "not_found_order": "Заказ не найден!",
            "confirm_text": "✅ Заказ подтвержден!",
            "rejected_text": "❌ Заказ отклонен!",
            "not_found_order": "❗ Заказ не найден!",
            "order_data": lambda name, size, soni, order_price, product_price, status: f"<b>Информация о заказе:</b>\n\n<b>Название продукта:</b> {name}\n<b>Размер продукта:</b> {size}\n<b>Номер заказа:</b> {soni}\n<b>Цена продукта:</b> {product_price} USD\n<b>Цена заказа:</b> {order_price} USD\n<b>Статус:</b> {status}",
            "alert_order_user": lambda order_id, status: f"❗ Ваш цифровой заказ {order_id} {'подтвержден!' if status == 'confirmed' else 'отклонено!'}"
        },
        "reports": {
            "main_text": "Какой тип отчета вы хотите?",
            "main_menu": ("Ежедневно", "Еженедельно", "Ежемесячно", "Ежегодно", "🏠 Главное меню"),
            "admin_menu": ("Ежедневно", "Еженедельно", "Ежемесячно", "Ежегодно", "❌ Отклонено", "🕙 Неподтверждено", "Товары", "🏠 Главное меню"),
            "not_report": "Приказа подготовить отчет нет!",
            "alert": "Выберите одно из меню."
        },
        "debtor_message": lambda name, balans : f"❗ Вы должны {name}!\n\nВаш аккаунт: {utils.pulni_qismlash(balans)} USD",
        "manage_products":{
            "main_text": "Вы в управлении продуктом!",
            "main_menus": ("Добавить продукт", "Удаление продукта", "Изменить количество товара", "🏠 Главное меню")
        },
        "change_count_product": {
            "input_text": "Введите идентификатор продукта.",
            "count_input_text": "Введите новое количество товара.",
            "changed_count_product": "✅Количество товаров обновлено!",
            "enter_an_integer": "Butun son kiriting.",
            "not_find_product": "❗ Такой товар не найден!"
        },
        "del_product": {
            "input_text": "Введите идентификатор продукта.",
            "deleted_product": "❗ Товар удален!",
            "not_find_product": "❗ Такой товар не найден!"
        },
        "changed_count_product_message": lambda name, size: f"Обновлено количество товаров из {name} размера {size}!",  
        "changed_count_order_message": lambda order_id, user_name: f"{user_name} обновил количество своего заказа №{order_id}!",  
        "deleted_product_message": lambda name, size: f"{name} размер товара {size} удален из базы данных!",
        "deleted_order_message": lambda order_id, user_name: f"❗ {user_name} {order_id} raqamli buyurtmasini bekor qildi!",
        "new_product_message": lambda name: f"🆕 <b>В базу добавлен новый товар!\nИмя:</b> {name}",
        "sending_message_users_count": lambda sending_users : f"✅ {sending_users} пользователям отправлено сообщение!",
        "basket": {
            "order_manage_menu": ("🔢 Изменить сумму", "❌ Отмена заказа"),
            "order_data": lambda name, size, soni, price, date, order_id: (
                f"<b>{order_id} числовая информация о заказе:</b>\n\n"
                f"<b>Имя:</b> {name}\n"
                f"<b>Размер:</b> {size}\n"
                f"<b>Количество:</b> {soni}\n"
                f"<b>Расходы:</b> {utils.pulni_qismlash(price)} USD\n"
                f"<b>Дата заказа:</b> {date.split()[0]}"
                ),
            "not_found_order": "❗ Заказ на данный товар не найден!",
            "empty_basket": "🛒 Корзина пуста",
            "send_order_count": "На сколько вы хотите изменить количество заказов!",
            "changed_order_count": "✅ Изменено количество заказов!",
            "deleted_order": "❗ Заказ удален!",
            "error_order_count": "❗ Неверно указано количество заказов. Попробуйте еще раз.",
            "save_order": lambda balans: f"Информация о вашем заказе обновлена.!\n Ваш счет: {utils.pulni_qismlash(balans)} USD",
        
            
        },
        "add_product": {
            "send_name": "Введите название продукта.",
            "saved_name": "Название бренда сохранено!",
            "send_size": "Введите размер продукта.",
            "save_not_size": "товар данного наименования и размера имеется в базе!",
            "saved_size": "Размер товара сохранен!",
            "send_soni": "Введите номер товара,",
            "send_digit": "Отправьте мне номер.",
            "saved_soni": "Количество сохраненных предметов!",
            "send_price": "Введите цену товара.",
            "saved_price": "Цена товара принята!",
            "send_img1": "Отправить первое изображение товара или сохранить текущую информацию?",
            "send_imges_menu": ("✅ Отправить", "🚫 Отмена"),
            "saved_img": "Изображение сохранено, отправить другое изображение?",
            "product_data": lambda name, size, soni, price: (
            f"<b>Имя:</b> {name}\n"
            f"<b>Размер:</b> {size}\n"
            f"<b>Число:</b> {soni}\n"
            f"<b>Расходы:</b> {utils.pulni_qismlash(price)} USD\n"),
            "confirm_text": "Подтвердить информацию?",
            "confirm_data_menu": ("✅ Подтверждение", "🚫 Отмена"),
            "saved_product": lambda id: f"<b>✅ Товар сохранен!</b>\n\n<b>ID:</b>{id}"
        },
        "products_user": {
            "main_menu_text": "📦 Вы находитесь в разделе товары! Выберите продукт.",
             "product_data": lambda name, size, soni, price: (
                f"Информация о продукте:\n\n"
                f"<b>Nomi:</b> {name}\n"
                f"<b>O'lchami:</b> {size}\n"
                f"<b>Soni:</b> {soni}\n"
                f"<b>Narxi:</b> {utils.pulni_qismlash(price)} USD\n"),
            "not_found_product": "❗ Этого товара не существует!",
            "add_order_menu": "savatga qo'shish",
            "send_order_soni": "Сколько товаров вы хотите купить?",
            "save_order": lambda balans: f"<b>Ваш заказ добавлен в корзину!</b>\nВаш счет {utils.pulni_qismlash(balans)} USD!",
            "new_order": lambda order_id: f"<b>Новый заказ:</b> ID {order_id}",
            "error_order_count": "❗ Неверно указано количество заказов. Попробуйте еще раз."
        }

    },
    "QA": {
        "search_inline_mode": "🔎 Qıdırıw ",
        "confirm_menu": ("✅ Jiberiw", "🚫 Bıykarlaw "),
        "not_know": "❗ Buyrıqtı tushunmadim! ",
        "sign up": {
            "lan": "Atiñizdi kiritiñ",
            "name": "Siz haqqıńızda adminga xabar berdim. Esabıńız tastıyıqlanishini kuting.",
            "user_status_change_to_member_user_message": "✅ Esabıńız tastıyıqlandi!",
            "user_status_change_to_member_admin_message": "✅ Paydalanıwshı esabı tastıyıqlandi!",
            "user_status_change_to_none_user_message": "❗️ Esabıńızdı bloklandi!",
            "user_status_change_to_none_admin_message": "❗️ Paydalanıwshı esabı bloklandi!",
            "bug": "❗️ Paydalanıwshına xabar jiberiwde qanday da mashqala boldı. Men onı bazadan tazalap jiberdim. Itimal, ol botni bloklaǵan bolıwı múmkin.",
            "old_message": "❗️ Bul xabar eski hám paydalanıwshı allqachon bazzadan óshirip jiberilgen!"
            },
        "block_user": "❗ Sizdiń esabıńız tastıyıqlanmagan!",
        "start": {
            "admin": "Assalawma aleykum, admin!",
            "user": "Assalawma aleykum "
        },
        "main_menu": {
            "text": "🏠 Tiykarǵı menyu",
            "menu":  ("📦 Ónimler", " 🛒 Sebet", " 📬 Meniń buyirtmalarim", "📒 Esabatlar", " 📂 Qosimsha zatlar", "⚙️ Sazlamalar")
        },
        "additional_items": {
            "main_text": "Kerekli menyunı saylań.",
            "menu": ("⚖️ Balans", " 💲USD stul", "🧾 Bahalar kestesi", " 🏠 Tiykarǵı menyu"),
            "dollar_kursi": lambda kurs_rate, date: f"<b>VALYUTA KURSI:\n\n1 USD - {kurs_rate} USD\n\n<b>Ózbekstan Respublikası Oraylıqa banki - {date}</b>",
            "balans": lambda balans: f"<b>Esabıńız: </b>\n\n{balans} USD"
        },  
        "confirm_order": {
            "in_text": "Vvedite nomer zakaza.",
            "confirm_menu": ("✅ Tastıyıqlaw ", "❌ Bıykarlaw "),
            "confirm_text": "✅ Buyırtpa tastıyıqlandi!",
            "rejected_text": "❌ Buyırtpa biykarlaw etildi!",
            "not_found_user": "Paydalanıwshı tabilǵan zatdı ",
            "not_found_product": "Ónim tabilǵan zatdı!",
            "not_found_order": "❗ Buyırtpa tabilǵan zatdı!",
            "order_data": lambda name, size, soni, order_price, product_price, status: f"<b>Buyırtpa maǵlıwmatları:</b>\n\n<b>Ónim atı:</b> {name}\n<b>Ónim ólshemi:</b> {size}\n<b>Buyırtpa sanı:</b> {soni}\n<b>Ónim bahası:</b> {product_price} USD\n<b>Buyırtpa bahası:</b> {order_price} USD\n<b>Jaǵdayı:</b> {status}",
            "alert_order_user": lambda order_id, status: f"❗ Sizdiń {order_id} cifrlı buyırtpańız {'tasdiqlandi!' if status == 'confirmed' else 'biykarlaw etildi!'}"
        },
        "settings": {
            "main_text": "Neni sazlamoqchisiz?",
            "main_menu": ("Tildi sazlaw", "🏠 Tiykarǵı menyu"),
            "admin_menu": ("Tildi sazlaw", "Qarızdarlıq bildiriw xatı waqtın sazlaw", "Qarızdarlıq limitini sazlaw", "🏠 Tiykarǵı menyu"),
            "set_lan_text": "Tildi saylań.",
            "changed_lan_text": "Til qaraqalpaq tiline ózgertirildi!",
            "change_time_text": lambda soat, minut: f"Ámeldegi saylanǵan waqıt {soat}:{minut}",
            "change_limit_text": lambda limit: f"Házirgi limit: {limit} USD\n\nJańa limitni jiberiń."
        },
        "debtor_message": lambda name, balans : f"❗ {name} siz qarızdarsız! \n\nEsabıńız: {utils.pulni_qismlash(balans)} USD",
        "my_orders": {
            "main_menu":  ("🆕 Jańa", "❌ Biykarlaw etilgen", "🕙 Tastıyıqlanmagan", "🏠 Tiykarǵı menyu"),
            "main_text": "Qaysı jaǵday daǵı buyırtpalarıńız kestein olmoqchisiz?",
            "not_new_order": "❗ Aqırǵı 1 háptede buyırtpa berilmegen!",
            "not_canceled_orders": "❗ Biykar etilgen buyırtpalar tabilǵan zatdı!",
            "not_pending_orders": "❗ Tastıyıqlanishi kutilayotgan buyırtpalar tabilǵan zatdı!",
            "my_orders_table_columns": ("user_ID", "At","Buyırtpa nomeri", "Ónim atı ", "Ónim ólshemi", "Buyırtpalar sanı ", "Buyırtpa bahası ", "Buyırtpa waqtı ", "Buyırtpa jaǵdayı"),
        },
        "manage_users": {
            "main_text": "Paydalanıwshılardı basqarıw menyusidasiz!",
            "main_menu": ("Paydalanıwshılar kestesi", "Xabar jiberiw", "🏠 Tiykarǵı menyu"),
            "input_message_text": "Xabarni yuboring.",
            "acc_message": "✅ Xabar qabıllandı!",
            "users_list_text": "Paydalanıwshın saylań.",
            "not_found_user": "❗ Paydalanıwshı tabilǵan zatdı!",
            "manage_user_text": "Buyıruqni saylań.",
            "mission_acc": "✅ Wazıypa atqarıldı!",
            "acc_alerts_for_user": {
                "del": "Siz bazadan óshirildingiz!",
                "block": "Siz bloklandingiz!",
                "active": "Sizdiń esabıńız aktivlestirildi!",
                "addadmin": "Siz admin etildińiz!",
                "rmAdmin": "Siz adminlikdan alındıńız!"
            },
            "thisIsAdmin": "Bul paydalanıwshı aldın admin etilgen!",
            "thisIsNotAdmin": "Bul paydalanıwshı admin etilmegen!",
            "user_data": lambda name, id, balans, status: f"Paydalanıwshı maǵlıwmatları:\n\nAt-familya: {name}\nID: {id}\nBalans: {utils.pulni_qismlash(balans)} USD\nJaǵdayı: {status if status else 'block'}",
            "manage_user_menu": ("Bazadan óshiriw", "Bloklaw", "Aktivlestiriw", "Admin qılıw", "Adminlikdan alıw", "Balanstı toltırıw ", "⬅ Kestege qaytıw "),
            "send_summa": "Qansha pul qosamız?"

        },
        "admin_menu": ("Buyırtpanı kóriw", "Esabatlar ", "Ónimler", "Paydalanıwshılar ", "⚙️ Sazlamalar"),
        "reports": {
            "main_text": "Qaysı túrdegi esabattı olmoqchisiz?",
            "main_menu": ("Kúnlik", "Háptelik", "Aylıq", "Jıllıq", "🏠 Tiykarǵı menyu"),
            "admin_menu": ("Kúnlik", "Háptelik", "Aylıq", "Jıllıq", "❌ Biykarlaw etilgen", "🕙 Tastıyıqlanmagan", "Tovarlar", "🏠 Tiykarǵı menyu"),
            "not_report": "Esabat tayarlaw ushın buyırtpa joq!",
            "alert": "Menyulardan birin saylań."
        },
        "manage_products":{
            "main_text": "Siz ónimlerdi basqarıw bólimindesiz!",
            "main_menus": ("Ónim qosıw", "Ónim óshiriw", "Ónim muǵdarın ózgertiw", "🏠 Tiykarǵı menyu")
        },
        "change_count_product": {
            "input_text": "Ónimdi idsini kiritiń.",
            "count_input_text": "Ónimdiń jańa muǵdarın kiritiń.",
            "changed_count_product": "✅ Ónim muǵdarı jańalandi!",
            "enter_an_integer": "Butun son kiriting.",
            "not_find_product": "❗ Hesh narse tabilmadi!"
        },
        
        "del_product": {
            "input_text": "Ónimdi idsini kiritiń.",
            "deleted_product": "❗ Ónim óshirildi!",
            "not_find_product": "❗ Hesh narse tabilmadi!"
        },
        "changed_count_product_message": lambda name, size: f"{name} ónimi {size} ólshemi muǵdarı jańalandi!",  
        "changed_count_order_message": lambda order_id, user_name: f"{user_name}, {order_id} sanlı buyırtpasınıń muǵdarın jańaladi!",  
        "deleted_product_message": lambda name, size: f"{name} ónimi {size} ólshemi bazadan óshirildi!",
        "deleted_order_message": lambda order_id, user_name: f"❗ {user_name} {order_id} raqamli buyurtmasini bekor qildi!",
        "new_product_message": lambda name: f"🆕 <b>Bazaǵa jańa tavar qosıldı!\nAtı:</b> {name}",
        "sending_message_users_count": lambda sending_users : f"✅ {sending_users} paydalanıwshına xabar jiberildi!",
        "basket": {
            "order_manage_menu": ("🔢 Muǵdarın ózgertiw", "❌ Buyırtpanı bıykarlaw "),
            "order_data": lambda name, size, soni, price, date, order_id: (
                f"<b>{order_id} cifrlı buyırtpa maǵlıwmatları:</b>\n\n"
                f"<b>Atı:</b> {name}\n"
                f"<b>Ólshemi:</b> {size}\n"
                f"<b>Sanı:</b> {soni}\n"
                f"<b>Bahası:</b> {utils.pulni_qismlash(price)} USD\n\n"
                f"<b>Buyırtpa berilgen sáne:</b> {date.split()[0]}"
                ),
            "not_found_order": "❗ Bul nomdagi ónimge buyırtpa tabilǵan zatdı!",
            "empty_basket": "🛒 Sebet bos",
            "send_order_count": "Buyırtpalar sanın neshege ózgertiwchisiz!",
            "changed_order_count": "✅ Buyırtpalar sanı ózgertirildi!",
            "deleted_order": "❗ Buyırtpa óshirildi!",
            "error_order_count": "❗ Buyırtpalar sanı nadurıs kiritilgen. Qayta urınıp kóriń.",
            "save_order": lambda balans: f"Buyırtpańız maǵlıwmatları jańalandi!\n Esabıńız: {utils.pulni_qismlash(balans)} USD",
        
        },
        "add_product": {
            "send_name": "Tavar atınıń kiritiń.",
            "saved_name": "Tavar atı saqlandi!",
            "send_size": "Tavar ólshemin kiritiń.",
            "save_not_size": "Bul nomdagi hám ólshem degi tavar bazada ámeldegi!",
            "saved_size": "Tavar ólshemi saqlandi!",
            "send_soni": "Tavar sanın kiritiń.",
            "send_digit": "Maǵan san jiberiń.",
            "saved_soni": "Ónimler sanı saqlandi!",
            "send_price": "Ónim bahasın kiritiń.",
            "saved_price": "Ónim bahası qabıllandı!",
            "send_img1": "Ónimdıń 1-suwretin jiberiń yamasa ámeldegi maǵlıwmatlardı saqlaysizmi?",
            "send_imges_menu": ("✅ Jiberiw", "🚫 Bıykarlaw "),
            "saved_img": "Súwret saqlandi, taǵı súwret jiberasizmi?",
            "product_data": lambda name, size, soni, price: (
                f"<b>Atı:</b> {name}\n"
                f"<b>Ólshemi:</b> {size}\n"
                f"<b>Sanı:</b> {soni}\n"
                f"<b>Bahası:</b> {utils.pulni_qismlash(price)} USD\n"),
            "confirm_text": "Maǵlıwmatlardı tastıyıqlaysizmi?",
            "confirm_data_menu": ("✅ Tastıyıqlaw", "🚫 Bıykarlaw"),
            "saved_product": lambda id: f"<b>✅ Ónim saqlandi!</b>\n\n<b>ID:</b> {id}"
        },
        "products_user": {
            "main_menu_text": " 📦 Ónimler bólimindesiz! Ónimdi saylań.",
             "product_data": lambda name, size, soni, price: (
                f"Tavar maǵlıwmatları:\n\n"
                f"<b>Atı:</b> {name}\n"
                f"<b>Ólshemi:</b> {size}\n"
                f"<b>Sanı:</b> {soni}\n"
                f"<b>Bahası:</b> {utils.pulni_qismlash(price)} USD\n\n"),
            "not_found_product": "❗ Bul nomdagi tavar joq!",
            "add_order_menu": "savatga qo'shish",
            "send_order_soni": "Ónimdan neshe harid qılajaqsız?",
            "save_order": lambda balans: f"Buyırtpa sebetke taslandı!\nEsabıńızde {utils.pulni_qismlash(balans)} USD",
            "new_order": lambda order_id: f"<b>Jańa buyırtpa:</b> ID {order_id}",
            "error_order_count": "❗ Buyırtpalar sanı nadurıs kiritilgen. Qayta urınıp kóriń."
            
        }

    }
}