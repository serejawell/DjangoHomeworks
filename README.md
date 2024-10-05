# homework_19.2
# homework_20.1

Эта работа предназначена для реализации ORM в проекте Django.
Создали подключение к бд, описали 2 модели (Продукты, Категории) и сделали несколько примеров с этими моделями.
Дампнули все данные в отдельный файл.
Реализовали кастомную команду по загрузке данных из нашего json файла.

# homework 20.2
Создали контроллер и шаблон, которые отвечают за вывод страницы на каждый товар. 
Создали контроллер и шаблон, в котором происходит вывод всех продуктов в цикле.
Выделили базовый шаблон
Вывели изображение для каждого товара

# homework 21.1
Переписали контроллеры с FBV на CBV в приложении catalog, там же добавили счетчик просмотров + разные кнопки на создание, удаление, редактирование. 
Создали новое приложение blog, в котором аналогично создали контроллеры на CBV, сделали модель Post, для создания постов в нашем блоге.
Реализовали кнопки удаления, создания, просмотра и редактирования.
Сделали счетчик просмотров 
Создали фильтр через queryset для просмотра опубликованного контента 

# homework 22.1
Реализовали форму для создания продукта пользователем. Сделали список из запрещенных слов, которые можно упоминать в названии продукта.
Создали модель контроля Версий, реализовали создание версий продукта пользователем с формами (Продукт, название версии. Номер верссии генерируется автоматически, при помощи метода save в модели Version)
