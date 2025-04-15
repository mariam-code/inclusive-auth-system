import polib

translations = {
    "Welcome to SecureBank": {
        "fr": "Bienvenue sur SecureBank",
        "es": "Bienvenido a SecureBank",
        "ar": "مرحبًا بك في SecureBank",
        "yo": "Kaabo si SecureBank",
        "zh": "欢迎使用 SecureBank",
        "bn": "SecureBank-এ স্বাগতম",
        "pl": "Witamy w SecureBank",
        "hi": "SecureBank में आपका स्वागत है"
    },
    "Don’t have an account? Register here": {
        "fr": "Vous n'avez pas de compte ? Inscrivez-vous ici",
        "es": "¿No tienes una cuenta? Regístrate aquí",
        "ar": "ليس لديك حساب؟ سجل هنا",
        "yo": "Ṣe o ko ni iroyin? Forukọsilẹ nibi",
        "zh": "没有账户？在这里注册",
        "bn": "আপনার কি অ্যাকাউন্ট নেই? এখানে নিবন্ধন করুন",
        "pl": "Nie masz konta? Zarejestruj się tutaj",
        "hi": "क्या आपके पास खाता नहीं है? यहाँ पंजीकरण करें"
    },
    "One-Time Password": {
        "fr": "Mot de passe à usage unique",
        "es": "Contraseña de un solo uso",
        "ar": "رمز مرور لمرة واحدة",
        "yo": "Ọrọigbaniwọle lẹ́ẹ̀kan ṣoṣo",
        "zh": "一次性密码",
        "bn": "একবারের পাসওয়ার্ড",
        "pl": "Jednorazowe hasło",
        "hi": "एक बार का पासवर्ड"
    },
    "Face ID Verification": {
        "fr": "Vérification d'identité par reconnaissance faciale",
        "es": "Verificación de identidad facial",
        "ar": "التحقق من الهوية باستخدام الوجه",
        "yo": "Ìmúlòlùfẹ̀ ojú",
        "zh": "人脸识别验证",
        "bn": "ফেস আইডি যাচাইকরণ",
        "pl": "Weryfikacja tożsamości twarzy",
        "hi": "फेस आईडी सत्यापन"
    },
    "For demonstration only: Please upload a face image to verify your identity.": {
        "fr": "Démonstration uniquement : veuillez télécharger une image faciale pour vérifier votre identité.",
        "es": "Solo demostración: por favor sube una imagen facial para verificar tu identidad.",
        "ar": "لأغراض العرض فقط: يرجى تحميل صورة للوجه للتحقق من هويتك.",
        "yo": "Fun àfihàn nikan: Jọwọ gbe aworan oju silẹ lati jẹrisi idanimọ rẹ.",
        "zh": "仅用于演示：请上传人脸照片以验证身份。",
        "bn": "শুধুমাত্র প্রদর্শনের জন্য: আপনার পরিচয় যাচাই করতে একটি মুখের ছবি আপলোড করুন।",
        "pl": "Tylko demonstracja: prześlij zdjęcie twarzy, aby zweryfikować swoją tożsamość.",
        "hi": "केवल प्रदर्शन के लिए: कृपया अपनी पहचान सत्यापित करने के लिए एक चेहरा छवि अपलोड करें।"
    },
    "In real applications, live webcam capture should be used for secure authentication.": {
        "fr": "Dans les applications réelles, la capture en direct par webcam doit être utilisée pour une authentification sécurisée.",
        "es": "En aplicaciones reales, debe usarse captura en vivo por webcam para autenticación segura.",
        "ar": "في التطبيقات الفعلية، يجب استخدام التقاط مباشر بالكاميرا للتحقق الآمن.",
        "yo": "Ninu awọn ohun elo gidi, lilo webcam laaye yẹ ki o ṣee lo fun ìmúlòlùfẹ̀ to ni aabo.",
        "zh": "在真实应用中，应使用实时摄像头进行安全身份验证。",
        "bn": "বাস্তব অ্যাপ্লিকেশনগুলিতে, নিরাপদ প্রমাণীকরণের জন্য লাইভ ওয়েবক্যাম ব্যবহার করা উচিত।",
        "pl": "W prawdziwych aplikacjach należy używać kamery internetowej na żywo do bezpiecznej autoryzacji.",
        "hi": "वास्तविक अनुप्रयोगों में सुरक्षित प्रमाणीकरण के लिए लाइव वेबकैम का उपयोग किया जाना चाहिए।"
    },
    "Authenticated.": {
        "fr": "Authentifié.",
        "es": "Autenticado.",
        "ar": "تم التحقق.",
        "yo": "Ti jẹrisi.",
        "zh": "已验证。",
        "bn": "প্রমাণিত হয়েছে।",
        "pl": "Uwierzytelniono.",
        "hi": "सत्यापित।"
    },
    "Upload Face Image": {
        "fr": "Télécharger une image faciale",
        "es": "Subir imagen facial",
        "ar": "تحميل صورة الوجه",
        "yo": "Gbe aworan oju silẹ",
        "zh": "上传人脸图像",
        "bn": "মুখের ছবি আপলোড করুন",
        "pl": "Prześlij zdjęcie twarzy",
        "hi": "चेहरे की छवि अपलोड करें"
    },
    "Processing image...": {
        "fr": "Traitement de l'image...",
        "es": "Procesando imagen...",
        "ar": "جارٍ معالجة الصورة...",
        "yo": "Ṣiṣayẹwo aworan...",
        "zh": "正在处理图像...",
        "bn": "ছবি প্রক্রিয়া হচ্ছে...",
        "pl": "Przetwarzanie obrazu...",
        "hi": "छवि प्रोसेस की जा रही है..."
    },
    "Logout": {
        "fr": "Déconnexion",
        "es": "Cerrar sesión",
        "ar": "تسجيل الخروج",
        "yo": "Jade",
        "zh": "登出",
        "bn": "লগআউট",
        "pl": "Wyloguj się",
        "hi": "लॉग आउट"
    },
    "Register": {
        "fr": "S'inscrire",
        "es": "Registrarse",
        "ar": "تسجيل",
        "yo": "Forukọsilẹ",
        "zh": "注册",
        "bn": "নিবন্ধন",
        "pl": "Zarejestruj się",
        "hi": "पंजीकरण करें"
    },
    "⏰ Face too old. Please upload a recent image taken within the last 60 seconds.": {
    "fr": "⏰ Image trop ancienne. Veuillez télécharger une image récente prise dans la dernière minute.",
    "es": "⏰ Imagen demasiado antigua. Por favor, sube una imagen tomada en el último minuto.",
    "ar": "⏰ الصورة قديمة جدًا. يرجى تحميل صورة حديثة تم التقاطها خلال آخر 60 ثانية.",
    "yo": "⏰ Aworan ti pẹ. Jọwọ gbe aworan tuntun ti a ya ni iṣẹju kan sẹyin silẹ.",
    "zh": "⏰ 图像太旧。请上传最近60秒内拍摄的图像。",
    "bn": "⏰ ছবিটি পুরনো। অনুগ্রহ করে গত ৬০ সেকেন্ডে তোলা একটি সাম্প্রতিক ছবি আপলোড করুন।",
    "pl": "⏰ Obraz jest zbyt stary. Prześlij zdjęcie zrobione w ciągu ostatnich 60 sekund.",
    "hi": "⏰ छवि पुरानी है। कृपया पिछले 60 सेकंड के भीतर ली गई हाल की छवि अपलोड करें।"
},
}

for lang in translations["Welcome to SecureBank"].keys():
    po_path = f"translations/{lang}/LC_MESSAGES/messages.po"
    po = polib.pofile(po_path)
    updated = 0
    for msgid, langs in translations.items():
        entry = po.find(msgid)
        if entry:
            entry.msgstr = langs[lang]
            updated += 1
    po.save()
    print(f"✅ {lang.upper()}: {updated} translations updated")

print("\nNow run this to compile:")
print("python -m babel.messages.frontend compile --directory=translations")
