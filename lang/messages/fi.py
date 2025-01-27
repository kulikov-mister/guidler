fi = {
    'welcome_message': """
        🎉 Tervetuloa <b>Guidler</b>iin! 🎉
        🚀 Olemme iloisia, että luotatte meihin 🥰.
        🙃 Missä roolissa haluaisit liittyä meihin?
    """,
    'start_admin_message': """
        🔆 Tervetuloa ylläpitäjä <b>Guidleriin</b>! 🔆
        🚀 Olemme iloisia, että luotat meihin 🥰.
    """,
    'start_message': """Tervetuloa takaisin <b>Guidleriin</b>! 🚀 Olemme iloisia, että luotat meihin 🥰.""",
    'choose_category': """Valitse kategoria""",
    'choose_instruction': """Valitse ohje""",
    'choose_channel_message': """Valitse kanava/ryhmä ohjeillesi""",
    'sent_name_category': """Syötä kategorian nimi:""",
    'sent_lang_category': """Syötä kaksikirjaimisessa muodossa kieli kategorialle (ru, en jne.):""",
    'category_crating': """Kategoria luotu onnistuneesti.""",
    'invalid_language_code': """Virheellinen kielikoodi. Anna oikea kaksikirjaiminen koodi.""",
    'help_message': """Siispä, tässä on lista komennoista:""",
    'registration_required_message': """Tämän toiminnon käyttämiseksi on rekisteröidyttävä.""",
    'bot_not_admin_message': """Bot ei ole ylläpitäjä tässä keskustelussa. Tee botista ylläpitäjä ja yritä uudelleen.""",
    'instruction_added_message': """
        <b>Ohje lisätty onnistuneesti.</b>
        - <i>Nyt kun olet luonut ohjeen, voit luoda siihen käyttäjien suodattamiseksi kategorioita.
        - Tätä varten käytä: /add_category</i>
    """,
    'instruction_already_exists_message': """
        <b>Ohje tällä nimellä on jo olemassa tässä kanavassa.</b>
        <i>Ole hyvä ja käytä toista nimeä.</i>
    """,
    'category_creating': """Ohje luodaan. Odota hetki...""",
    'invalid_group_id_message': """Annettu ryhmän ID on väärä. Ole hyvä ja tarkista ja yritä uudelleen.""",
    'sent_name_instruction': """Lähettäkää ohjeenne nimi.""",
    'bot_not_in_chat_message': """<b>Botti ei voi saada tietoa chatin jäsenestä.</b> Varmista, että botti on lisätty ryhmään ja yritä uudelleen.""",
    'instruction_added_error': """<b>Virhe ohjeen luomisessa:</b> sellainen on jo olemassa.""",
    'inline_chat_selection': """
        Vahvista valintasi:
        
        - <b>Nimi</b>: {group_name},
        - <b>ID</b>: {group_id}
    """,
    'no_rights_in_channel': """Botilla ei ole oikeuksia viestien täyteen muokkaamiseen valitussa ryhmässä/kanavassa.""",
    'your_channel_name': """Teidän nimi:""",
    'code_404': """Captcha ei läpäisty""",
    'code_404_description': """Käynnistä toiminto uudelleen muuttamatta generoitua koodia nähdäksesi tuloksesi.""",
    'switch_pm_text': """Valitse ryhmä/kanava alla olevasta luettelosta""",
    'channel_approved': """Valinta vahvistettu!""",
    'category_name_too_long': """Kategorian nimi on liian pitkä! (enintään 20 merkkiä)""",
    'not_instruction_for_faq': """Sinulla ei ole ohjeita, joihin voi lisätä usein kysyttyjä kysymyksiä.""",
    'not_categories_for_faq': """Sinulla ei ole kategorioita, joihin voit lisätä UKK:ta.""",
    'choose_instruction_for_faq': """Valitse ohjeet, joihin haluat lisätä UKK:n.""",
    'choose_category_for_faq': """Valitse FAQ-kategoria.""",
    'enter_faq_name': """
        Syötä UKK:n nimi.
        <i>Tämä nimi näkyy ohjeiden linkkien postauksessa</i>
    """,
    'enter_faq_content': """Syötä UKK:n sisältö (voi olla tekstiä tai mediatiedosto).""",
    'faq_added_successfully': """UKK on lisätty onnistuneesti.""",
    'back_to_instruction': """Takaisin ohjeisiin""",
    'navigation_error': """Sivujen navigointivirhe.""",
    'micro_plan_faq': """
        <b>Hei, tässä on mikrosuunnitelma nykyiseen vaiheeseen:</b>
        
        1. Valitse ohjeet FAQ-postaukseen.
        2. Valitse kategoria ohjeista.
        3. Anna nimi FAQ-postaukselle.
        4. Lähetä FAQ-postauksen sisältö.
        5. FAQ-postauksesi on lisätty ja valmis julkaistavaksi.
    """,
    'micro_plan_add_instruction': """
        <b>Hei, tässä on mikrosuunnitelma nykyiselle vaiheelle:</b>
        
        1. Valitse tai lisää kanava/ryhmä botille.
        2. Lisää botti valitun kanavan/ryhmän adminiksi.
        3. Vahvista kanavan/ryhmän valinta inline-tilassa.
        4. Anna ohjeen nimi.
        5. Päätä prosessi. Ilmoitus lähetetään, jos botti poistetaan kanavalta/ryhmästä.
    """,
    'micro_plan_add_category': """
        <b>Hei, tässä on mikrosuunnitelma nykyiselle askeleelle:</b>
        
        1. Lähetä komento /add_category aloittaaksesi prosessin.
        2. Valitse ohje, johon kategoria liitetään.
        3. Anna kategorian nimi (enintään 20 merkkiä).
        4. Ilmoita kategorian kaksikirjaiminen kielikoodi (esimerkiksi 'en' tai 'ru').
        5. Tarkistuksen ja vahvistuksen jälkeen kategoria lisätään.
    """,
    'not_instruction_for_publish': """Ei ohjeita julkaisemista varten!""",
    'micro_plan_publish': """
        <b>Hei, tässä on mikrosuunnitelma nykyiselle askeleelle:</b>
        
        1. Valitse ohje FAQ-postaukseen.
        2. Valitse kategoria ohjeissa.
        3. Valitse julkaisun tyyppi.
        4. Tarkistuksen ja vahvistuksen jälkeen ohjeesi julkaistaan. Saat ilmoituksen prosessin päättymisestä.
    """,
    'select_type_for_publish_pro': """
        <b>Valitse julkaisun tyyppi</b>
        <i>Kaikki julkaisutyypit ovat käytettävissäsi</i>
    """,
    'select_type_for_publish_not_pro': """
        <b>Valitse julkaisun tyyppi</b>
        <i>Voit julkaista vain yhden sivun</i>
    """,
    '': """Sure, I can help with that. Please provide the text you need translated to Finnish.""",
}
