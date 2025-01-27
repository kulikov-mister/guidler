tr = {
    'welcome_message': """
        🎉 <b>Guidler</b>'a hoş geldiniz! 🎉
        🚀 Bize güvendiğiniz için mutluyuz 🥰.
        🙃 Bize hangi durumda katılmak istersiniz?
    """,
    'start_admin_message': """
        🔆 <b>Guidler</b>'e hoş geldiniz admin! 🔆
        🚀 Bize güvendiğiniz için mutluyuz 🥰.
    """,
    'start_message': """
        🔆 <b>Guidler</b>'a Hoş Geldiniz! 🔆
        🚀 Bize güvendiğiniz için çok mutluyuz 🥰.
    """,
    'choose_category': """Kategoriyi seçin""",
    'choose_instruction': """Talimatı seçin""",
    'choose_channel_message': """Talimatınız için bir kanal/grup seçin""",
    'sent_name_category': """Kategori adını girin:""",
    'sent_lang_category': """<b>Kategoriler için dil kodunu iki harfli formatda girin (ru, en vb.):</b>""",
    'category_crating': """<b>Kategori başarıyla oluşturuldu.</b>""",
    'invalid_language_code': """Yanlış dil kodu. Lütfen doğru iki harfli kodu girin.""",
    'help_message': """İşte komutların listesi:""",
    'registration_required_message': """Bu özelliği kullanabilmek için kaydolmanız gerekmektedir.""",
    'bot_not_admin_message': """Bot bu sohbette yönetici değil. Lütfen botu yönetici yapın ve tekrar deneyin.""",
    'instruction_added_message': """
        Talimat başarıyla eklendi.
        - Artık bir talimat oluşturduğunuzda, kullanıcıları filtrelemek için kategoriler oluşturabilirsiniz.
        - Bunun için kullanın: /add_category
    """,
    'instruction_already_exists_message': """
        <b>Bu kanalda bu isimde zaten bir talimat var.</b>
        <i>Lütfen başka bir isim kullanın.</i>
    """,
    'category_creating': """Talimat oluşturuluyor. Lütfen bekleyin...""",
    'invalid_group_id_message': """Yanlış grup kimliği sağlandı. Lütfen kontrol edin ve tekrar deneyin.""",
    'sent_name_instruction': """Talimatınız için bir ad gönderin.""",
    'bot_not_in_chat_message': """Bot, sohbet üyesi hakkındaki bilgilere erişemiyor. Lütfen botun gruba eklendiğinden emin olun ve tekrar deneyin.""",
    'instruction_added_error': """<b>Oluşturma hatası:</b> Böyle biri zaten var.""",
    'inline_chat_selection': """
        Onaylayın Seçiminizi:
        
        - <b>Adı</b>: {group_name},
        - <b>ID</b>: {group_id}
    """,
    'no_rights_in_channel': """Botun seçilen grup/kanalda mesajları tamamen düzenleme yetkisi yok.""",
    'your_channel_name': """Başlığınız:""",
    'code_404': """Captcha geçilemedi""",
    'code_404_description': """Sonuçlarınızı görmek için üretilen kodu değiştirmeden fonksiyonu yeniden başlatın.""",
    'switch_pm_text': """Aşağıdaki listeden bir grup/kanal seçin""",
    'channel_approved': """Seçim onaylandı!""",
    'category_name_too_long': """Kategori adı çok uzun! (20 karaktere kadar)""",
    'not_instruction_for_faq': """Ekleyebileceğiniz FAQ bulunan bir talimatınız yok.""",
    'not_categories_for_faq': """Ekleyebileceğiniz FAQ kategorileriniz bulunmuyor.""",
    'choose_instruction_for_faq': """FAQ eklemek istediğiniz talimatı seçin.""",
    'choose_category_for_faq': """SSS için bir kategori seçin.""",
    'enter_faq_name': """
        FAQ Başlığını Girin.
        <i>Bu başlık, talimat bağlantılarının gönderisinde yansıtılacaktır</i>
    """,
    'enter_faq_content': """SSS içeriğini giriniz (metin veya medya dosyası olabilir).""",
    'faq_added_successfully': """SSS başarıyla eklendi.""",
    'back_to_instruction': """Talimatlara geri dön""",
    'navigation_error': """Sayfa geziniminde hata.""",
    'micro_plan_faq': """
        <b>Merhaba, işte mevcut adıma ilişkin mikro plan:</b>
        
        1. SSS gönderisi için talimatı seçin.
        2. Talimatta kategoriyi seçin.
        3. SSS gönderisi için bir başlık girin.
        4. SSS gönderisinin içeriğini gönderin.
        5. SSS gönderiniz eklenecek ve yayımlanmaya hazır olacak.
    """,
    'micro_plan_add_instruction': """
        <b>Merhaba, işte mevcut adım için mikro plan:</b>
        
        1. Bir kanal/grup seçin veya ekleyin.
        2. Seçilen kanal/gruba botu bir admin olarak ekleyin.
        3. Kanal/grup seçimini çevrimiçi modda onaylayın.
        4. Talimatın adını girin.
        5. İşlemi tamamlayın. Eğer bot kanal/gruptan kaldırılırsa bir bildirim gönderilecektir.
    """,
    'micro_plan_add_category': """
        <b>Merhaba, işte mevcut adıma dair mikro plan:</b>
        
        1. Süreci başlatmak için /add_category komutunu gönderin.
        2. Kategoriye bağlanacak talimatı seçin.
        3. Kategori adını girin (en fazla 20 karakter).
        4. Kategori dilinin iki harfli kodunu belirtin ('en' veya 'ru' gibi).
        5. Bilgiler kontrol edildikten ve onaylandıktan sonra kategori eklenecek.
    """,
    'not_instruction_for_publish': """Yayınlamak için talimat yok!""",
    'micro_plan_publish': """
        <b>Merhaba, işte mevcut adıma göre mikro plan:</b>
        
        1. SSS gönderisi için talimatı seçin.
        2. Talimatta kategoriyi seçin.
        3. Yayın türünü seçin.
        4. Kontrol ve onaydan sonra talimatınız yayınlanacak. İşlemin tamamlandığına dair bir bildirim alacaksınız.
    """,
    'select_type_for_publish_pro': """
        <b>Yayın türünü seçin</b>
        <i>Tüm yayın türleri size açıktır</i>
    """,
    'select_type_for_publish_not_pro': """
        Yayın tipini seçin
        Sadece 1 sayfa yayınlayabilirsiniz
    """,
    '': """Sure, I can help with that. Please provide the text you need translated into Turkish.""",
}
