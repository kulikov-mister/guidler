de = {
    'welcome_message': """
        🎉 Willkommen bei <b>Guidler</b>! 🎉
        🚀 Wir freuen uns, dass Sie uns Ihr Vertrauen schenken 🥰.
        🙃 In welchem Status möchten Sie sich uns anschließen?
    """,
    'start_admin_message': """Willkommen, Admin, bei <b>Guidler</b>! 🚀 Wir freuen uns, dass Sie uns Ihr Vertrauen schenken 🥰.""",
    'start_message': """Willkommen zurück bei <b>Guidler</b>! 🚀 Wir freuen uns, dass Sie uns Ihr Vertrauen schenken 🥰.""",
    'choose_category': """Wählen Sie eine Kategorie aus""",
    'choose_instruction': """Wählen Sie die Anleitung aus""",
    'choose_channel_message': """Wählen Sie den Kanal/die Gruppe für Ihre Anleitung aus""",
    'sent_name_category': """Geben Sie den Kategoriennamen ein:""",
    'sent_lang_category': """Geben Sie die Sprache für die Kategorie im zweibuchstabigen Format ein (ru, en usw.):""",
    'category_crating': """<b>Kategorie erfolgreich erstellt.</b>""",
    'invalid_language_code': """Ungültiger Sprachcode. Bitte geben Sie einen korrekten zweibuchstabigen Code ein.""",
    'help_message': """Also, hier ist die Liste der Befehle:""",
    'registration_required_message': """Um diese Funktion zu nutzen, müssen Sie sich registrieren.""",
    'bot_not_admin_message': """Der Bot ist kein Administrator in diesem Chat. Bitte machen Sie den Bot zum Administrator und versuchen Sie es erneut.""",
    'instruction_added_message': """
        <b>Anleitung erfolgreich hinzugefügt.</b>
        - <i>Jetzt, da Sie eine Anleitung erstellt haben, können Sie Kategorien erstellen, um Benutzer zu filtern.
        - Verwenden Sie dazu: /add_category</i>
    """,
    'instruction_already_exists_message': """
        <b>Eine Anleitung mit diesem Namen existiert bereits in diesem Kanal.</b>
        <i>Bitte verwenden Sie einen anderen Namen.</i>
    """,
    'category_creating': """Die Anleitung wird erstellt. Bitte warten...""",
    'invalid_group_id_message': """Es wurde eine ungültige Gruppen-ID angegeben. Bitte überprüfen Sie diese und versuchen Sie es erneut.""",
    'sent_name_instruction': """Senden Sie den Namen für Ihre Anweisung.""",
    'bot_not_in_chat_message': """Der Bot kann nicht auf die Chatmitgliederinformationen zugreifen. Stellen Sie sicher, dass der Bot zur Gruppe hinzugefügt wurde, und versuchen Sie es erneut.""",
    'instruction_added_error': """<b>Fehler beim Erstellen der Anleitung:</b> Eine solche existiert bereits.""",
    'inline_chat_selection': """
        Bestätigen Sie Ihre Auswahl:
        
        - <b>Name</b>: {group_name},
        - <b>ID</b>: {group_id}
    """,
    'no_rights_in_channel': """Der Bot hat keine Berechtigung zur vollständigen Bearbeitung von Nachrichten in der ausgewählten Gruppe/dem ausgewählten Kanal.""",
    'your_channel_name': """Ihr Name:""",
    'code_404': """Captcha nicht bestanden""",
    'code_404_description': """Starten Sie die Funktion neu, ohne den generierten Code zu ändern, um Ihre Ergebnisse zu sehen.""",
    'switch_pm_text': """Wählen Sie eine Gruppe/einen Kanal aus der Liste unten aus.""",
    'channel_approved': """Auswahl bestätigt!""",
    'category_name_too_long': """Kategoriename ist zu lang! (bis zu 20 Zeichen)""",
    'not_instruction_for_faq': """Sie haben keine Anweisungen, zu denen FAQ hinzugefügt werden können.""",
    'not_categories_for_faq': """Sie haben keine Kategorien, denen FAQs hinzugefügt werden können.""",
    'choose_instruction_for_faq': """Wählen Sie die Anleitung aus, zu der Sie ein FAQ hinzufügen möchten.""",
    'choose_category_for_faq': """Wählen Sie eine Kategorie für FAQ aus.""",
    'enter_faq_name': """
        Geben Sie den Namen des FAQ ein.
        *Dieser Name wird in den Anweisungslinks im Beitrag angezeigt.*
    """,
    'enter_faq_content': """Geben Sie den Inhalt des FAQ ein (kann Text oder eine Mediendatei sein).""",
    'faq_added_successfully': """FAQ erfolgreich hinzugefügt.""",
    'back_to_instruction': """Zurück zu den Anweisungen""",
    'navigation_error': """Navigationsfehler auf den Seiten.""",
    'micro_plan_faq': """
        <b>Hallo, hier ist der Mikroplan für den aktuellen Schritt:</b>
        
        1. Wählen Sie die Anleitung für den FAQ-Beitrag aus.
        2. Wählen Sie die Kategorie in der Anleitung aus.
        3. Geben Sie den Titel für den FAQ-Beitrag ein.
        4. Senden Sie den Inhalt des FAQ-Beitrags.
        5. Ihr FAQ-Beitrag wird hinzugefügt und ist bereit zur Veröffentlichung.
    """,
    'micro_plan_add_instruction': """
        <b>Hallo, hier ist der Mikroplan für den aktuellen Schritt:</b>
        
        1. Wählen Sie einen Kanal/Gruppe für den Bot aus oder fügen Sie einen hinzu.
        2. Fügen Sie den Bot als Admin in den ausgewählten Kanal/Gruppe hinzu.
        3. Bestätigen Sie die Auswahl des Kanals/der Gruppe im Inline-Modus.
        4. Geben Sie den Namen der Anleitung ein.
        5. Schließen Sie den Prozess ab. Eine Benachrichtigung wird gesendet, falls der Bot aus dem Kanal/der Gruppe entfernt wird.
    """,
    'micro_plan_add_category': """
        <b>Hallo, hier ist ein Kurzplan für den aktuellen Schritt:</b>
        
        1. Senden Sie den Befehl /add_category, um den Prozess zu starten.
        2. Wählen Sie die Anleitung aus, an die die Kategorie gebunden wird.
        3. Geben Sie den Namen der Kategorie ein (nicht mehr als 20 Zeichen).
        4. Geben Sie den zweibuchstabigen Sprachcode der Kategorie an (zum Beispiel 'de' oder 'ru').
        5. Nach der Überprüfung und Bestätigung der Informationen wird die Kategorie hinzugefügt.
    """,
    'not_instruction_for_publish': """Keine Anweisungen zur Veröffentlichung!""",
    'micro_plan_publish': """
        <b>Hallo, hier ist ein Mikroplan für den aktuellen Schritt:</b>
        
        1. Wählen Sie die Anleitung für den FAQ-Beitrag aus.
        2. Wählen Sie die Kategorie in der Anleitung aus.
        3. Wählen Sie den Veröffentlichungstyp aus.
        4. Nach Überprüfung und Bestätigung wird Ihre Anleitung veröffentlicht. Sie erhalten eine Benachrichtigung, sobald der Prozess abgeschlossen ist.
    """,
    'select_type_for_publish_pro': """
        <b>Wählen Sie den Veröffentlichungstyp</b>
        <i>Ihnen stehen alle Arten von Veröffentlichungen zur Verfügung</i>
    """,
    'select_type_for_publish_not_pro': """
        <b>Wählen Sie den Veröffentlichungstyp</b>
        <i>Sie können nur 1 Seite veröffentlichen</i>
    """,
    '': """
        Of course! Please provide the text you need translated to German, and I'll assist you with the translation.
    """,
}
