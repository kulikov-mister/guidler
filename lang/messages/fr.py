fr = {
    'welcome_message': """
        🎉 Bienvenue chez <b>Guidler</b> ! 🎉
        🚀 Nous sommes ravis que vous nous fassiez confiance 🥰.
        🙃 Dans quel statut souhaitez-vous nous rejoindre ?
    """,
    'start_admin_message': """
        Bienvenue, administrateur, sur <b>Guidler</b> ! 🔆
        🚀 Nous sommes heureux que vous nous fassiez confiance 🥰.
    """,
    'start_message': """
        🔆 Bienvenue de retour chez <b>Guidler</b> ! 🔆
        🚀 Nous sommes ravis que vous nous fassiez confiance 🥰.
    """,
    'choose_category': """Sélectionnez une catégorie""",
    'choose_instruction': """
        Sélectionnez l'instruction
    """,
    'choose_channel_message': """Sélectionnez le canal/groupe pour votre instruction""",
    'sent_name_category': """Entrez le nom de la catégorie :""",
    'sent_lang_category': """Entrez le code de langue pour la catégorie au format à deux lettres (ru, en, etc.) :""",
    'category_crating': """La catégorie a été créée avec succès.""",
    'invalid_language_code': """Code de langue incorrect. Veuillez entrer un code à deux lettres valide.""",
    'help_message': """Alors, voici la liste des commandes :""",
    'registration_required_message': """
        Pour utiliser cette fonction, il est nécessaire de s'inscrire.
    """,
    'bot_not_admin_message': """
        Le bot n'est pas administrateur dans ce chat. Veuillez rendre le bot administrateur et essayez de nouveau.
    """,
    'instruction_added_message': """
        <b>La notice a été ajoutée avec succès.</b>
        - <i>Maintenant que vous avez créé la notice, vous pouvez y créer des catégories pour filtrer les utilisateurs.
        - Pour cela, utilisez : /add_category</i>
    """,
    'instruction_already_exists_message': """
        <b>Une instruction portant ce nom existe déjà sur cette chaîne.</b>
        <i>Veuillez utiliser un autre nom, s'il vous plaît.</i>
    """,
    'category_creating': """
        La création de l'instruction est en cours. Veuillez patienter...
    """,
    'invalid_group_id_message': """
        <b>ID de groupe fourni est incorrect.</b>
        Veuillez vérifier et essayer à nouveau.
    """,
    'sent_name_instruction': """Envoyez le titre de votre instruction.""",
    'bot_not_in_chat_message': """Le bot ne peut pas accéder aux informations sur le membre du chat. Assurez-vous que le bot est ajouté au groupe et essayez à nouveau.""",
    'instruction_added_error': """
        <b>Erreur lors de la création de l'instruction :</b> elle existe déjà.
    """,
    'inline_chat_selection': """
        Confirmez votre choix :
        
        - <b>Nom</b> : {group_name},
        - <b>ID</b> : {group_id}
    """,
    'no_rights_in_channel': """
        Le bot n'a pas les droits de modification complète des messages dans le groupe/canal sélectionné.
    """,
    'your_channel_name': """Votre nom :""",
    'code_404': """
        Le CAPTCHA n'a pas été validé.
    """,
    'code_404_description': """Redémarrez la fonction sans modifier le code généré pour voir vos résultats.""",
    'switch_pm_text': """Sélectionnez un groupe/canal dans la liste ci-dessous""",
    'channel_approved': """Le choix est confirmé !""",
    'category_name_too_long': """
        Le nom de la catégorie est trop long ! (jusqu'à 20 caractères)
    """,
    'not_instruction_for_faq': """
        Vous n'avez pas d'instructions auxquelles vous pouvez ajouter une FAQ.
    """,
    'not_categories_for_faq': """
        Vous n'avez pas de catégories auxquelles vous pouvez ajouter une FAQ.
    """,
    'choose_instruction_for_faq': """
        Sélectionnez l'instruction à laquelle vous souhaitez ajouter une FAQ.
    """,
    'choose_category_for_faq': """Sélectionnez une catégorie pour la FAQ.""",
    'enter_faq_name': """
        Saisissez le nom de la FAQ.
        <i>Ce nom apparaîtra dans le post sous forme de liens vers les instructions</i>
    """,
    'enter_faq_content': """Saisissez le contenu de la FAQ (peut être du texte ou un fichier multimédia).""",
    'faq_added_successfully': """FAQ ajouté avec succès.""",
    'back_to_instruction': """Retour aux instructions""",
    'navigation_error': """Erreur de navigation entre les pages.""",
    'micro_plan_faq': """
        <b>Bonjour, voici le micro-plan de l'étape actuelle :</b>
        
        1. Sélectionnez l'instruction pour le post FAQ.
        2. Choisissez une catégorie dans l'instruction.
        3. Entrez un titre pour le post FAQ.
        4. Envoyez le contenu du post FAQ.
        5. Votre post FAQ sera ajouté et prêt à être publié.
    """,
    'micro_plan_add_instruction': """
        <b>Bonjour, voici le micro-plan pour l'étape actuelle :</b>
        
        1. Sélectionnez ou ajoutez une chaîne/groupe pour le bot.
        2. Ajoutez le bot en tant qu'admin dans la chaîne/groupe sélectionné.
        3. Confirmez le choix de la chaîne/groupe en mode inline.
        4. Entrez le nom de l'instruction.
        5. Terminez le processus. Une notification sera envoyée si le bot est retiré de la chaîne/groupe.
    """,
    'micro_plan_add_category': """
        <b>Bonjour, voici le micro-plan de l'étape actuelle :</b>
        
        1. Envoyez la commande /add_category pour commencer le processus.
        2. Sélectionnez l'instruction à laquelle la catégorie sera liée.
        3. Entrez le nom de la catégorie (pas plus de 20 caractères).
        4. Indiquez le code à deux lettres de la langue de la catégorie (par exemple, 'fr' ou 'ru').
        5. Après vérification et confirmation des informations, la catégorie sera ajoutée.
    """,
    'not_instruction_for_publish': """
        Il n'y a pas d'instructions pour la publication !
    """,
    'micro_plan_publish': """
        <b>Bonjour, voici le micro-plan pour l'étape actuelle :</b>
        
        1. Sélectionnez l'instruction pour le post FAQ.
        2. Choisissez la catégorie dans l'instruction.
        3. Sélectionnez le type de publication.
        4. Après vérification et confirmation, votre instruction sera publiée. Vous recevrez une notification à la fin du processus.
    """,
    'select_type_for_publish_pro': """
        <b>Choisissez le type de publication</b>
        <i>Vous avez accès à tous les types de publications</i>
    """,
    'select_type_for_publish_not_pro': """
        <b>Choisissez le type de publication</b>
        <i>Vous ne pouvez publier qu'une seule page</i>
    """,
    '': """Please provide the text you want to be translated into French.""",
}
