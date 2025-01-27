cs = {
    'welcome_message': """
        🎉 Vítejte v <b>Guidler</b>! 🎉
        🚀 Jsme rádi, že nám důvěřujete 🥰.
        🙃 V jakém stavu byste se k nám chtěli připojit?
    """,
    'start_admin_message': """Vítejte, pane administrátore, na <b>Guidler</b>! 🚀 Jsme rádi, že nám důvěřujete 🥰.""",
    'start_message': """
        Vítejte zpět v <b>Guidler</b>! 🔆
        Jsme rádi, že nám důvěřujete 🥰.
    """,
    'choose_category': """Vyberte kategorii""",
    'choose_instruction': """Vyberte instrukci""",
    'choose_channel_message': """Vyberte kanál/skupinu pro vaši instrukci""",
    'sent_name_category': """Zadejte název kategorie:""",
    'sent_lang_category': """<b>Zadejte jazyk pro kategorii ve dvoupísmenném formátu (ru, en atd.):</b>""",
    'category_crating': """Kategorie byla úspěšně vytvořena.""",
    'invalid_language_code': """Nesprávný kód jazyka. Zadejte prosím správný dvoupísmenný kód.""",
    'help_message': """Takže, zde je seznam příkazů:""",
    'registration_required_message': """Pro použití této funkce je nutná registrace.""",
    'bot_not_admin_message': """Bot není v tomto chatu administrátorem. Prosím, udělejte bota administrátorem a zkuste to znovu.""",
    'instruction_added_message': """
        <b>Návod byl úspěšně přidán.</b>
        - <i>Nyní, když jste vytvořili návod, můžete v něm vytvořit kategorie pro filtrování uživatelů.
        - K tomu použijte: /add_category</i>
    """,
    'instruction_already_exists_message': """
        <b>Návod s tímto názvem již v tomto kanálu existuje.</b>
        <i>Prosím, použijte jiný název.</i>
    """,
    'category_creating': """Návod se vytváří. Prosím, čekejte...""",
    'invalid_group_id_message': """Bylo zadáno nesprávné ID skupiny. Prosím, zkontrolujte a zkuste to znovu.""",
    'sent_name_instruction': """Pošlete název pro vaši instrukci.""",
    'bot_not_in_chat_message': """Bot nemůže získat přístup k informacím o členu chatu. Ujistěte se, že bot je přidán do skupiny a zkuste to znovu.""",
    'instruction_added_error': """<b>Chyba při vytváření návodu:</b> již existuje.""",
    'inline_chat_selection': """
        Potvrďte svou volbu:
        
        - <b>Název</b>: {group_name},
        - <b>ID</b>: {group_id}
    """,
    'no_rights_in_channel': """Bot nemá práva na úplnou úpravu zpráv ve vybrané skupině/kanálu.""",
    'your_channel_name': """Vaše název:""",
    'code_404': """Captcha nebyla úspěšně ověřena.""",
    'code_404_description': """Restartujte funkci bez změny generovaného kódu, abyste viděli své výsledky.""",
    'switch_pm_text': """Vyberte skupinu/kanál ze seznamu níže.""",
    'channel_approved': """Výběr potvrzen!""",
    'category_name_too_long': """Název kategorie je příliš dlouhý! (do 20 znaků)""",
    'not_instruction_for_faq': """Nemáte žádné instrukce, ke kterým lze přidat FAQ.""",
    'not_categories_for_faq': """Nemáte žádné kategorie, do kterých by bylo možné přidat FAQ.""",
    'choose_instruction_for_faq': """Vyberte návod, ke kterému chcete přidat FAQ.""",
    'choose_category_for_faq': """Vyberte kategorii pro FAQ.""",
    'enter_faq_name': """
        Zadejte název FAQ.
        <i>Tento název se objeví v příspěvku jako odkazy na instrukce</i>.
    """,
    'enter_faq_content': """Zadejte obsah FAQ (může být textem nebo mediálním souborem).""",
    'faq_added_successfully': """FAQ byly úspěšně přidány.""",
    'back_to_instruction': """Zpět k instrukcím""",
    'navigation_error': """Chyba v navigaci stránek.""",
    'micro_plan_faq': """
        <b>Ahoj, tady je mikroplán pro aktuální krok:</b>
        
        1. Vyberte instrukci pro FAQ příspěvek.
        2. Vyberte kategorii v instrukci.
        3. Zadejte název pro FAQ příspěvek.
        4. Odešlete obsah FAQ příspěvku.
        5. Váš FAQ příspěvek bude přidán a připraven k publikaci.
    """,
    'micro_plan_add_instruction': """
        <b>Ahoj, tady je mikroplán pro současný krok:</b>
        
        1. Vyberte nebo přidejte kanál/skupinu pro bota.
        2. Přidejte bota jako admina do vybraného kanálu/skupiny.
        3. Potvrďte výběr kanálu/skupiny v inline režimu.
        4. Zadejte název instrukce.
        5. Dokončete proces. Pokud bude bot odstraněn z kanálu/skupiny, bude odesláno oznámení.
    """,
    'micro_plan_add_category': """
        <b>Ahoj, tady je mikroplán pro současný krok:</b>
        
        1. Pošlete příkaz /add_category pro zahájení procesu.
        2. Vyberte instrukci, ke které bude kategorie přiřazena.
        3. Zadejte název kategorie (ne více než 20 znaků).
        4. Uveďte dvoupísmenný kód jazyka kategorie (například 'en' nebo 'ru').
        5. Po kontrole a potvrzení informací bude kategorie přidána.
    """,
    'not_instruction_for_publish': """<b>Není k dispozici žádný návod k publikování!</b>""",
    'micro_plan_publish': """
        <b>Ahoj, zde je mikroplán pro aktuální krok:</b>
        
        1. Vyberte instrukci pro FAQ příspěvek.
        2. Vyberte kategorii v instrukci.
        3. Vyberte typ publikace.
        4. Po kontrole a potvrzení bude vaše instrukce publikována. Obdržíte oznámení o dokončení procesu.
    """,
    'select_type_for_publish_pro': """
        Vyberte typ publikace
        Máte k dispozici všechny typy publikací
    """,
    'select_type_for_publish_not_pro': """
        Vyberte typ publikace
        Můžete publikovat pouze 1 stránku
    """,
    '': """Sure, I can help with that. What text would you like me to translate into Czech?""",
}
