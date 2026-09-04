import telebot
from telebot import types

# Initialize your bot with the API token
bot = telebot.TeleBot("token")
global_language = 'english'
# Define a dictionary to store language greetings and menu options
language_texts = {
    'english': {
        'greeting': """Welcome to our training bot! I'm here to help you achieve your fitness goals and support you on the path to a healthy lifestyle.

I'm ready to offer you personalized workouts, nutrition advice, and motivational tips. Whether you want to lose weight, gain muscle mass, or improve your endurance, I'm here to help you succeed.

Feel free to ask me any questions or make any requests. Let's make your journey to health and fitness exciting and effective together!

Are you ready to start training?""",
        'menu': "\nPlease select the category you are interested in:\n\n"
                "For home workouts, type /home_training\n"
                "For various diets, type /diet\n"
                "For specific training programs, type /training",
        'options': ['Home training', 'Diets', 'Training for specific bodyparts']
    },
    'russian': {
        'greeting': """Добро пожаловать в нашего тренировочного бота! Я здесь, чтобы помочь вам достичь ваших фитнес-целей и поддерживать вас на пути к здоровому образу жизни.

Я готов предложить вам персонализированные тренировки, советы по питанию и мотивационные подсказки. Независимо от того, хотите ли вы сбросить вес, увеличить мышечную массу или улучшить свою выносливость, я здесь, чтобы помочь вам добиться успеха.

Не стесняйтесь задавать мне любые вопросы или запросы. Давайте вместе сделаем ваш путь к здоровью и фитнесу увлекательным и результативным!

Готовы начать тренировки?
""" ,
        'menu': "\nВыберите ту категорию, которая вас интересует:\n\n"
                "Для просмотра тренировок в домашних условиях /home_training\n"
                "Для просмотра различных диет /diet\n"
                "Для просмотра специфичных тренировок /training",
        'options': ['Домашняя тренировка', 'Диеты', 'Тренировки для разных частей тела']
    },
    'kazakh': {
        'greeting': """Біздің тренировка ботымызға қош келдіңіз! Мен сіздің фитнес мақсаттарыңызға жетуге көмек көрсету үшін мұнда өмір салтын бақылауға көмек көрсетемін.

Мен сізге жеке тренировкалар, тамақ және мотивациялық үлгілер ұсынуға дайынмын. Сіз сөйлесіп отырған ақпарат бойынша салмақтарыңызды толықтыру, мышқа массасын көбейту немесе қызметтілігіңізді жақсарту қажет болса, мен сізге сәтті болуға көмек көрсету үшін бармын.

Сіздің сұрауларыңызды жасау немесе сұрауларыңызды жасауға шынайы. Біз сіздің денсаулық және фитнеске жолдыжарды жақсарту үшін көмек көрсетеміз!

Тренировкаларды бастауға дайынсыз ба?""" ,
        'menu': "\nТөмендегі қалаған категорияны таңдаңыз:\n\n"
                "Үйде жұмыс жасау  үшін /home_training\n"
                "Көптеген диеталар үшін /diet\n"
                "Белгілі тренировкалар /training",
        'options': ['Үйде жұмыс', 'диета', 'Белгілі тренировкалар']
    }
}
home_training = {
    'english': {"""guides for home workouts
1. **Plan Your Workouts**: Determine in advance which exercises and how many repetitions you intend to do. Planning will help you stay on track and avoid skipping sessions.
2. **Use Your Body Weight**: Many exercises can be done using only your body weight. Squats, push-ups, pull-ups on a bar - all of these are excellent options for home workouts.
3. **Utilize Equipment**: If you have a home gym or even just dumbbells or resistance bands, make use of them. They can add variety to your workouts.
4. **Watch Video Tutorials**: There are plenty of video tutorials and online platforms where experienced instructors share home workout tips. Choose ones that suit your fitness level and goals.
5. **Don't Forget Warm-up and Stretching**: Warm-up helps prepare your body for exercise and reduces the risk of injury, while stretching after a workout helps reduce muscle soreness and improve flexibility.
6. **Consistency and Regularity**: It's important to train regularly to achieve results. Set a goal to workout a certain number of times per week and stick to that schedule.
7. **Set Goals**: Determine what specific results you want to achieve, whether it's improving physical fitness, losing weight, or gaining muscle mass. Continuously work towards those goals.
8. **Rest**: Give your body time to recover after workouts. Regular rest days are as important as the workouts themselves.
"""

    },
    'russian': {"""Гайды для тренировок дома:
Планируйте свои тренировки: Заранее определите, какие упражнения и сколько повторений вы собираетесь делать. Планирование поможет вам оставаться на правильном пути и избежать пропусков.
Используйте свой вес: Множество упражнений можно делать, используя только собственный вес тела. Приседания, отжимания, подтягивания на турнике - все это отличные варианты для тренировок дома.
Используйте оборудование: Если у вас есть домашний тренажерный зал или даже просто гантели или эспандер, воспользуйтесь ими. Они могут добавить разнообразия в ваши тренировки.
Изучайте видеоуроки: Существует множество видеоуроков и онлайн-платформ, где опытные инструкторы делятся советами по тренировкам дома. Выберите те, которые подходят вашему уровню подготовки и ваши цели.
Не забывайте про разминку и растяжку: Разминка помогает подготовить тело к тренировке и снижает риск травм, а растяжка после тренировки помогает уменьшить мышечную боль и улучшить гибкость.
Постоянство и регулярность: Важно тренироваться регулярно, чтобы добиться результатов. Поставьте себе цель тренироваться определенное количество раз в неделю и придерживайтесь этого графика.
Поставьте себе цели: Определите, какие именно результаты вы хотите достичь, будь то улучшение физической формы, снижение веса или увеличение мышечной массы. Постоянно работайте на их достижение.
Отдыхайте: Дайте своему телу время на восстановление после тренировок. Регулярные дни отдыха так же важны, как и тренировки.
"""
    },'kazakh': {"""Үйде жаттығуға арналған нұсқаулықтар:
1.	Жаттығуларыңызды жоспарлаңыз: қандай жаттығулар мен қанша қайталау жасайтындығыңызды алдын-ала анықтаңыз. Жоспарлау сізге дұрыс жолда қалуға және жіберіп алудан аулақ болуға көмектеседі.
2.	Өз салмағыңызды пайдаланыңыз: көптеген жаттығуларды тек өз дене салмағыңызбен жасауға болады. Скват, итеру, көлденең жолақты тарту - бұл үйде жаттығудың тамаша нұсқалары.
3.	Жабдықты пайдаланыңыз: егер сізде үйде жаттығу залы немесе тіпті гантельдер немесе қарсылық белдеуі болса, оларды пайдаланыңыз. Олар сіздің жаттығуларыңызға әртүрлілік қоса алады.
4.	Бейне оқулықтарды үйреніңіз: тәжірибелі нұсқаушылар үйде жаттығу бойынша кеңестермен бөлісетін көптеген бейне оқулықтар мен онлайн платформалар бар. Сіздің дайындық деңгейіңізге және мақсаттарыңызға сәйкес келетіндерді таңдаңыз.
5.	Жылыну мен созылуды ұмытпаңыз: жылыну денені жаттығуға дайындауға көмектеседі және жарақат алу қаупін азайтады, ал жаттығудан кейін созылу бұлшықет ауырсынуын азайтуға және икемділікті жақсартуға көмектеседі.
6.	Тұрақтылық пен жүйелілік: нәтижеге жету үшін үнемі жаттығу жасау маңызды. Аптасына бірнеше рет жаттығуды мақсат етіп қойыңыз және осы кестені ұстаныңыз.
7.	Өзіңізге мақсат қойыңыз: фитнес, салмақ жоғалту немесе бұлшықет массасының жоғарылауы болсын, нақты қандай нәтижелерге қол жеткізгіңіз келетінін анықтаңыз. Оларға жету үшін үнемі жұмыс жасаңыз.
8.	Демалыңыз: жаттығудан кейін денеңізді қалпына келтіруге уақыт беріңіз. Тұрақты демалыс күндері жаттығу сияқты маңызды.
"""
    }
}
diets = {
    'english': {"""Тypes of diets:
1. **Weight Loss Diets**:
   - Ketogenic Diet: Low-carb, high-fat diet that aims to induce ketosis, a metabolic state where the body burns fat for fuel.
   - Low Glycemic Index (GI) Diet: Focuses on consuming foods with a low glycemic index to regulate blood sugar levels and control appetite.
   - Calorie-Restricted Diets: Based on controlling calorie intake to create a calorie deficit and promote weight loss.
   - Low-Fat or Low-Carb Diets: Involves restricting intake of specific macronutrients to reduce calories or regulate metabolism.
2. **Health-Related Diets**:
   - Mediterranean Diet: Based on the traditional dietary patterns of Mediterranean countries, rich in vegetables, fruits, olive oil, fish, and nuts.
   - DASH Diet (Dietary Approaches to Stop Hypertension): Recommended for controlling blood pressure and includes consumption of vegetables, fruits, low-fat dairy products, whole grains, and limited salt and sugar.
   - Vegan or Vegetarian Diet: Excludes or limits animal products in favor of plant-based foods.
3. **Specialized Diets**:
   - Skin-Improving Diets: Focuses on consuming foods rich in antioxidants, vitamins, and minerals like vitamin C and E, zinc, and selenium.
   - Diets for Managing Diabetes: Based on controlling carbohydrates and sugars to regulate blood glucose levels.
   - Anti-Inflammatory Diets: Include foods rich in anti-inflammatory components like omega-3 fatty acids, phytonutrients, and antioxidants.
4. **Sports-Specific Diets**:
   - Muscle-Building Diet: Involves increasing protein and calorie intake to support muscle growth.
   - Endurance-Enhancing Diet: Includes higher intake of carbohydrates to replenish glycogen stores used during physical activity.
Choosing the right diet depends on your goals, preferences, and individual needs. It's important to make dietary changes gradually and consult with a doctor or dietitian before making any significant changes to your eating habits.
"""

    },
    'russian': {"""Различные виды диет
1. **Диеты для похудения**:
   - Кетогенная диета: Низкое потребление углеводов, высокое потребление жиров, чтобы вывести организм в состояние кетоза, при котором он начинает использовать жиры в качестве основного источника энергии.
   - Диета с низким гликемическим индексом (ГИ): Основана на выборе продуктов с низким гликемическим индексом, чтобы уменьшить колебания уровня сахара в крови и контролировать аппетит.
   - Диеты с ограничением калорий: Основаны на контроле потребляемых калорий, чтобы создать дефицит калорий и способствовать потере веса.
   - Диеты с ограничением жиров или углеводов: Основаны на ограничении потребления определенных макронутриентов для снижения калорий или регулирования метаболизма.
2. **Диеты для здоровья**:
   - Средиземноморская диета: Основана на традиционной пищевой культуре средиземноморских стран, богатой овощами, фруктами, оливковым маслом, рыбой и орехами.
   - Диета DASH (Пищевая методика для остановки гипертонии): Рекомендуется для контроля артериального давления и включает в себя потребление овощей, фруктов, нежирных молочных продуктов, цельных зерен и ограничение соли и сахара.
   - Веганская или вегетарианская диета: Исключают продукты животного происхождения или ограничивают их потребление в пользу растительных продуктов.
3. **Диеты для специфических потребностей**:
   - Диеты для улучшения состояния кожи: Основаны на употреблении пищи, богатой антиоксидантами, витаминами и минералами, такими как витамин С и Е, цинк и селен.
   - Диеты для управления сахарным диабетом: Основаны на контроле углеводов и сахаров, чтобы регулировать уровень глюкозы в крови.
   - Диеты для снижения воспаления: Включают пищу, богатую антиинфламматорными компонентами, такими как омега-3 жирные кислоты, фитонутриенты и антиоксиданты.
4. **Спортивные диеты**:
   - Диета для набора мышечной массы: Основана на увеличении потребления белка и калорий для поддержания роста мышц.
   - Диета для увеличения выносливости: Включает в себя увеличение потребления углеводов для запаса гликогена, который используется во время физических упражнений.
Выбор подходящей диеты зависит от ваших целей, предпочтений и индивидуальных потребностей. Важно помнить, что любые изменения в рационе следует вносить постепенно, а лучше всего консультироваться с врачом или диетологом перед принятием решения.
"""
    },'kazakh': {"""Диетаның әртүрлі түрлері
1. ** Арықтауға арналған диеталар**:
   - Кетогендік диета: ағзаны кетоз күйіне келтіру үшін көмірсулардың аз мөлшері, майдың көп мөлшері, ол майларды негізгі энергия көзі ретінде қолдана бастайды.
   - Төмен гликемиялық индекс (gi) диетасы: қандағы қант деңгейінің ауытқуын азайту және тәбетті бақылау үшін гликемиялық индексі төмен тағамдарды таңдауға негізделген.
   - Калориясы шектеулі диеталар: калория тапшылығын тудыру және салмақ жоғалтуға ықпал ету үшін тұтынылатын калорияларды бақылауға негізделген.
   - Майларды немесе көмірсуларды шектейтін диеталар: калорияларды азайту немесе метаболизмді реттеу үшін белгілі бір макронутриенттерді тұтынуды шектеуге негізделген.
2. ** Денсаулыққа арналған диеталар**:
   - Жерорта теңізі диетасы: көкөністерге, жемістерге, зәйтүн майына, Балыққа және жаңғақтарға бай Жерорта теңізі елдерінің дәстүрлі тағамдық мәдениетіне негізделген.
   - DASH диетасы (гипертонияны тоқтатудың Тағамдық әдісі): қан қысымын бақылау үшін ұсынылады және көкөністерді, жемістерді, майсыз сүт өнімдерін, дәнді дақылдарды тұтынуды және тұз бен қантты шектеуді қамтиды.
   - Вегетариандық немесе вегетариандық диета: жануарлардан алынатын өнімдерді алып тастаңыз немесе өсімдік тектес тағамдардың пайдасына тұтынуды шектеңіз.
3. ** Нақты қажеттіліктерге арналған диеталар**:
   - Теріні жақсартуға арналған диеталар: антиоксиданттарға, С және Е дәрумені, мырыш және селен сияқты дәрумендер мен минералдарға бай тағамдарды жеуге негізделген.
   - Қант диабетін басқаруға арналған диеталар: қандағы глюкозаны реттеу үшін көмірсулар мен қанттарды бақылауға негізделген.
   - Қабынуды төмендететін диеталар: омега-3 май қышқылдары, фитонутриенттер және антиоксиданттар сияқты инфламматорға қарсы компоненттерге бай тағамдарды қамтиды.
4. ** Спорттық диеталар**:
   - Бұлшықет массасын арттыруға арналған Диета: бұлшықет өсуін қамтамасыз ету үшін ақуыз мен калорияны тұтынуды арттыруға негізделген.
   - Төзімділікті арттыруға арналған Диета: жаттығу кезінде қолданылатын гликогенді сақтау үшін көмірсулардың тұтынылуын арттыруды қамтиды.
Дұрыс диетаны таңдау сіздің мақсаттарыңызға, қалауларыңызға және жеке қажеттіліктеріңізге байланысты. Диетадағы кез-келген өзгерістер біртіндеп жасалуы керек екенін есте ұстаған жөн, бірақ шешім қабылдағанға дейін дәрігермен немесе диетологпен кеңескен дұрыс.
"""
    }
}

training_menu = {
    'english': {"""Training on
• Hands https://youtu.be/4CkVdu4z1HA?si=7tIYFGY44i7DwpG8
• Legs https://youtu.be/4CkVdu4z1HA?si=7tIYFGY44i7DwpG8
• Belly https://youtu.be/h8ctkfSx6R0?si=JkQoT8H2bpZUasH0
• Comprehensive https://youtu.be/qr8g-SBHef4?si=SC_D7XT2hlXzm6-0
"""

    },
    'russian': {"""Тренировки на
Руки https://youtu.be/4CkVdu4z1HA?si=7tIYFGY44i7DwpG8
Ноги https://youtu.be/4CkVdu4z1HA?si=7tIYFGY44i7DwpG8
Живот https://youtu.be/h8ctkfSx6R0?si=JkQoT8H2bpZUasH0
Комплексные https://youtu.be/qr8g-SBHef4?si=SC_D7XT2hlXzm6-0
"""
    },'kazakh': {"""Жаттығу
* Қолдар https://youtu.be/4CkVdu4z1HA?si=7tIYFGY44i7DwpG8
* Аяқ https://youtu.be/4CkVdu4z1HA?si=7tIYFGY44i7DwpG8
* Іш https://youtu.be/h8ctkfSx6R0?si=JkQoT8H2bpZUasH0
* Кешенді https://youtu.be/qr8g-SBHef4?si=SC_D7XT2hlXzm6-0
"""
    }
}
default = {
    'english': {"""Sorry, I didn't understand that command. Please type /start to begin.
"""
    },
    'russian': {"""Извините, я не понял эту команду. Пожалуйста, введите /start, чтобы начать.
"""
    },'kazakh': {"""Кешіріңіз, мен бұл команданы түсінбедім. Бастау үшін /start теріңіз.
"""
    }
}

greeting_all = "Hello! Please select your language: \nЗдраствуйте! Пожалуйста выберите язык: \nСәлем! тілді тандап алыныз:"

# Define a function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('English', callback_data='english'),
               types.InlineKeyboardButton('Russian', callback_data='russian'),
               types.InlineKeyboardButton('Kazakh', callback_data='kazakh'))
    bot.send_message(message.chat.id, greeting_all, reply_markup=markup)

# Define a function to handle language selection
@bot.callback_query_handler(func=lambda call: True)
def language_selection(call):
    selected_language = call.data
    global global_language 
    global_language = selected_language
    greeting_message = language_texts[selected_language]['greeting']
    menu_message = language_texts[selected_language]['menu']
    bot.send_message(call.message.chat.id, greeting_message)
    bot.send_message(call.message.chat.id, menu_message)

@bot.message_handler(commands=['home_training'])
def send_link(message):
    home_training_text = home_training[global_language]
    bot.send_message(message.chat.id, home_training_text)


@bot.message_handler(commands=['diet'])
def send_link(message):
    image_url = "https://www.spinecorrectioncenter.com/wp-content/uploads/2019/09/9-Benefits-of-Eating-a-Balanced-Diet_resized.png.webp"
    bot.send_photo(message.chat.id, image_url)
    diets_text = diets[global_language]
    bot.send_message(message.chat.id, diets_text)

@bot.message_handler(commands=['training'])
def send_alternative_response(message):
    training_text = training_menu[global_language]
    bot.send_message(message.chat.id, training_text)

@bot.message_handler(func=lambda message: True)
def default_response(message):
    default_text = default[global_language]
    bot.reply_to(message, default_text)


# Start the bot
bot.polling()
