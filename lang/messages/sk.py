sk = {
    'welcome_message': """
        🎉 Vitajte v <b>Guidler</b>! 🎉
        🚀 Sme radi, že nám dôverujete 🥰.
        🙃 V akom stave chcete k nám pristúpiť?
    """,
    'start_admin_message': """Vitajte, admin, v <b>Guidler</b>! 🚀 Sme radi, že nám dôverujete 🥰.""",
    'start_message': """S návratom do <b>Guidler</b>! 🚀 Tešíme sa, že nám dôverujete 🥰.""",
    'choose_category': """Vyberte kategóriu""",
    'choose_instruction': """Vyberte pokyn""",
    'choose_channel_message': """Vyberte kanál/skupinu pre vaše pokyny""",
    'sent_name_category': """Zadajte názov kategórie:""",
    'sent_lang_category': """Zadajte jazyk pre kategóriu vo formáte z dvoch písmen (ru, en atď.):""",
    'category_crating': """Kategória bola úspešne vytvorená.""",
    'invalid_language_code': """Nesprávny kód jazyka. Prosím, zadajte správny dvojpísmenný kód.""",
    'help_message': """Takže, tu je zoznam príkazov:""",
    'registration_required_message': """Pre použitie tejto funkcie je potrebné sa zaregistrovať.""",
    'bot_not_admin_message': """Bot nie je administrátorom v tomto chate. Prosím, urobte bota administrátorom a skúste to znova.""",
    'instruction_added_message': """
        <b>Návod bol úspešne pridaný.</b>
        - <i>Teraz, keď ste vytvorili návod, môžete v ňom vytvoriť kategórie pre filtrovanie používateľov.
        - Na to použite: /add_category</i>
    """,
    'instruction_already_exists_message': """
        <b>Návod s takýmto názvom už v tomto kanáli existuje.</b>
        <i>Prosím, použite iný názov.</i>
    """,
    'category_creating': """Návod sa vytvára. Prosím, čakajte...""",
    'invalid_group_id_message': """
        <b>Zadané nesprávne ID skupiny.</b>
        Prosím, skontrolujte a skúste znova.
    """,
    'sent_name_instruction': """Pošlite názov pre vaše pokyny.""",
    'bot_not_in_chat_message': """Bot nemôže získať prístup k informáciám o členovi chatu. Uistite sa, že bot je pridaný do skupiny a skúste to znova.""",
    'instruction_added_error': """<b>Chyba pri vytváraní inštrukcie:</b> taká už existuje.""",
    'inline_chat_selection': """
        Potvrďte svoj výber:
        
        - <b>Názov</b>: {group_name},
        - <b>ID</b>: {group_id}
    """,
    'no_rights_in_channel': """Bot nemá práva na úplné úpravy správ vo vybranej skupine/kanále.""",
    'your_channel_name': """Vaše názov:""",
    'code_404': """Captcha nebola prejdená""",
    'code_404_description': """Reštartujte funkciu bez zmeny generovaného kódu, aby ste videli svoje výsledky.""",
    'switch_pm_text': """Vyberte skupinu/kanál zo zoznamu nižšie""",
    'channel_approved': """Výber potvrdený!""",
    'category_name_too_long': """Názov kategórie je príliš dlhý! (do 20 znakov)""",
    'not_instruction_for_faq': """Nemáte žiadne inštrukcie, do ktorých možno pridať FAQ.""",
    'not_categories_for_faq': """Nemáte žiadne kategórie, do ktorých možno pridať FAQ.""",
    'choose_instruction_for_faq': """Vyberte inštrukciu, ku ktorej chcete pridať FAQ.""",
    'choose_category_for_faq': """Vyberte kategóriu pre FAQ.""",
    'enter_faq_name': """
        Zadajte názov FAQ.
        <i>Tento názov sa bude odrážať vo poste ako odkazy na inštrukcie.</i>
    """,
    'enter_faq_content': """Zadajte obsah FAQ (môže byť textom alebo mediálnym súborom).""",
    'faq_added_successfully': """FAQ úspešne pridané.""",
    'back_to_instruction': """Späť k pokynom""",
    'navigation_error': """Chyba v navigácii stránok.""",
    'micro_plan_faq': """
        <b>Ahoj, tu je mikroplán pre aktuálny krok:</b>
        
        1. Vyberte inštrukciu pre FAQ-príspevok.
        2. Vyberte kategóriu v inštrukcii.
        3. Zadajte názov pre FAQ-príspevok.
        4. Odošlite obsah FAQ-príspevku.
        5. Váš FAQ-príspevok bude pridaný a pripravený na publikovanie.
    """,
    'micro_plan_add_instruction': """
        <b>Ahoj, tu je mikroplán pre aktuálny krok:</b>
        
        1. Vyberte alebo pridajte kanál/skupinu pre bota.
        2. Pridajte bota ako admina do vybraného kanála/skupiny.
        3. Potvrďte výber kanála/skupiny v inline režime.
        4. Zadajte názov inštrukcie.
        5. Dokončite proces. Odošle sa oznámenie, ak je bot odstránený z kanála/skupiny.
    """,
    'micro_plan_add_category': """
        <b>Ahoj, tu je mikroplán pre aktuálny krok:</b>
        
        1. Pošlite príkaz /add_category na začatie procesu.
        2. Vyberte inštrukciu, ku ktorej bude kategória priradená.
        3. Zadajte názov kategórie (nie viac ako 20 znakov).
        4. Uveďte dvojpísmenný kód jazyka kategórie (napríklad 'en' alebo 'ru').
        5. Po kontrole a potvrdení informácií bude kategória pridaná.
    """,
    'not_instruction_for_publish': """Nie sú žiadne pokyny na publikovanie!""",
    'micro_plan_publish': """
        <b>Ahoj, tu je mikroplán pre aktuálny krok:</b>
        
        1. Vyberte inštrukciu pre FAQ príspevok.
        2. Vyberte kategóriu v inštrukcii.
        3. Vyberte typ publikácie.
        4. Po kontrole a potvrdení bude vaša inštrukcia publikovaná. O dokončení procesu dostanete oznámenie.
    """,
    'select_type_for_publish_pro': """
        Vyberte typ publikácie
        Máte k dispozícii všetky typy publikácií
    """,
    'select_type_for_publish_not_pro': """
        Vyberte typ publikácie
        Môžete zverejniť len 1 stranu
    """
}
