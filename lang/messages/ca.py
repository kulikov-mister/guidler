ca = {
    'welcome_message': """
        🎉 Benvingut a <b>Guidler</b>! 🎉
        🚀 Ens alegra que confieu en nosaltres 🥰.
        🙃 En quin estat voleu unir-vos a nosaltres?
    """,
    'start_admin_message': """
        🔆 Benvingut administrador a <b>Guidler</b>! 🔆
        🚀 Ens alegra que confiïs en nosaltres 🥰.
    """,
    'start_message': """
        🔆 Benvingut de nou a <b>Guidler</b>! 🔆
        🚀 Ens alegra que confieu en nosaltres 🥰.
    """,
    'choose_category': """Trieu una categoria""",
    'choose_instruction': """Seleccioneu les instruccions""",
    'choose_channel_message': """Seleccioneu el canal/grup per a la vostra instrucció""",
    'sent_name_category': """Introduïu el nom de la categoria:""",
    'sent_lang_category': """
        <b>Introduïu l'idioma per a la categoria en format de dues lletres (ru, en, etc.):</b>
    """,
    'category_crating': """
        La categoria s'ha creat amb èxit.
    """,
    'invalid_language_code': """
        Codi d'idioma incorrecte. Si us plau, introduïu un codi vàlid de dues lletres.
    """,
    'help_message': """Així que, aquí teniu la llista de comandes:""",
    'registration_required_message': """Per utilitzar aquesta funció, cal registrar-se.""",
    'bot_not_admin_message': """
        El bot no és administrador en aquest xat. Si us plau, feu l'bot administrador i torneu a provar.
    """,
    'instruction_added_message': """
        <b>La instrucció s'ha afegit amb èxit.</b>
        - <i>Ara que heu creat la instrucció, podeu crear categories per filtrar els usuaris.
        - Per això, utilitzeu: /add_category</i>
    """,
    'instruction_already_exists_message': """
        <b>Ja existeix una instrucció amb aquest nom en aquest canal.</b>
        <i>Si us plau, utilitzeu un altre nom.</i>
    """,
    'category_creating': """
        S'està creant la instrucció. Si us plau, espereu...
    """,
    'invalid_group_id_message': """
        <b>S'ha proporcionat un ID de grup incorrecte.</b>
        Si us plau, comproveu-ho i torneu-ho a intentar.
    """,
    'sent_name_instruction': """Envieu el nom per a la vostra instrucció.""",
    'bot_not_in_chat_message': """
        El bot no pot accedir a la informació del membre del xat. Assegureu-vos que el bot s'ha afegit al grup i torneu-ho a intentar.
    """,
    'instruction_added_error': """<b>Error en crear la instrucció:</b> ja existeix.""",
    'inline_chat_selection': """
        Confirmeu la vostra elecció:
        
        - <b>Nom</b>: {group_name},
        - <b>ID</b>: {group_id}
    """,
    'no_rights_in_channel': """
        El bot no té permisos per a l'edició completa de missatges al grup/canal seleccionat.
    """,
    'your_channel_name': """El vostre nom:""",
    'code_404': """
        La captcha no s'ha superat.
    """,
    'code_404_description': """Reinicieu la funció sense canviar el codi generat per veure els vostres resultats.""",
    'switch_pm_text': """Trieu un grup/canal de la llista a continuació""",
    'channel_approved': """
        La selecció s'ha confirmat!
    """,
    'category_name_too_long': """El nom de la categoria és massa llarg! (fins a 20 caràcters)""",
    'not_instruction_for_faq': """No teniu instruccions a les quals es pugui afegir preguntes freqüents.""",
    'not_categories_for_faq': """No teniu categories a les quals es pugui afegir un FAQ.""",
    'choose_instruction_for_faq': """Seleccioneu la instrucció a la qual voleu afegir el FAQ.""",
    'choose_category_for_faq': """Trieu una categoria per a les preguntes freqüents.""",
    'enter_faq_name': """
        Introduïu el títol del FAQ.
        *Aquest títol es reflectirà en el post com a enllaços d'instruccions*
    """,
    'enter_faq_content': """Introduïu el contingut de les preguntes freqüents (pot ser text o fitxer multimèdia).""",
    'faq_added_successfully': """Preguntes freqüents afegides amb èxit.""",
    'back_to_instruction': """Torna a les instruccions""",
    'navigation_error': """Error en la navegació per pàgines.""",
    'micro_plan_faq': """
        <b>Hola, aquí tens el microplà per a l'actual pas:</b>
        
        1. Trieu una instrucció per al post del FAQ.
        2. Seleccioneu una categoria en la instrucció.
        3. Introduïu un títol per al post del FAQ.
        4. Envieu el contingut del post del FAQ.
        5. El vostre post del FAQ serà afegit i llest per a la publicació.
    """,
    'micro_plan_add_instruction': """
        <b>Hola, aquí tens el microplà per a l'actual pas:</b>
        
        1. Trieu o afegiu un canal/grup per al bot.
        2. Afegiu el bot com a administrador al canal/grup seleccionat.
        3. Confirmeu la selecció del canal/grup en mode en línia.
        4. Introduïu el nom de la instrucció.
        5. Finalitzeu el procés. S'enviarà una notificació si el bot és eliminat del canal/grup.
    """,
    'micro_plan_add_category': """
        <b>Hola, aquí teniu el microplà per a l'actual pas:</b>
        
        1. Envieu l'ordre /add_category per començar el procés.
        2. Trieu la instrucció a la qual estarà vinculada la categoria.
        3. Introduïu el nom de la categoria (no més de 20 caràcters).
        4. Indiqueu el codi de dues lletres de l'idioma de la categoria (per exemple, 'en' o 'ru').
        5. Després de la revisió i confirmació de la informació, la categoria serà afegida.
    """,
    'not_instruction_for_publish': """No hi ha instruccions per publicar!""",
    'micro_plan_publish': """
        <b>Hola, aquí teniu el microplà per a l'actual pas:</b>
        
        1. Trieu la instrucció per al post del FAQ.
        2. Trieu la categoria en la instrucció.
        3. Trieu el tipus de publicació.
        4. Després de la revisió i confirmació, la vostra instrucció serà publicada. Rebreu una notificació quan el procés s'hagi completat.
    """,
    'select_type_for_publish_pro': """
        <b>Trieu el tipus de publicació</b>
        <i>Teniu disponibles tots els tipus de publicacions</i>
    """,
    'select_type_for_publish_not_pro': """
        <b>Trieu el tipus de publicació</b>
        <i>Podeu publicar només 1 pàgina</i>
    """,
    '': """
        Sure, I'd love to help. Please provide the text you'd like translated to Catalan.
    """,
}
