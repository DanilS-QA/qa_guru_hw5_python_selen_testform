from selene import browser, be, have, command
import os
image_path = os.path.abspath("text_file.txt")

def test_fill_form(setting_browser, browser_open):
    browser.should(have.title('DEMOQA'))

    # Проверка заголовка формы
    browser.element('.practice-form-wrapper h5').should(have.text('Student Registration Form'))

    # Заполнение поля Имя + проверка
    browser.element('#firstName').should(be.visible).type("Федор")
    browser.element('#firstName').should(have.value("Федор"))  # Проверка введенного значения

    # Заполнение поля Фамилия + проверка
    browser.element('#lastName').should(be.visible).type("Федоров")
    browser.element('#lastName').should(have.value("Федоров")) # Проверка введенного значения

    # Заполнение поля почта + проверка
    browser.element('#userEmail').should(be.visible).type("sychev.dg@gmail.com")
    browser.element('#userEmail').should(have.value("sychev.dg@gmail.com")) # Проверка введенного значения

    # Выбор радиокнопки (Gender) + проверка
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#gender-radio-1').should(be.selected)  # Проверка, что кнопка выбрана

    # Заполнение телефона + проверка
    browser.element('#userNumber').should(be.visible).type("9123456789")
    browser.element('#userNumber').should(have.value("9123456789")) # Проверка введенного значения

    # Выбор даты рождения + проверка
    # 1. Открыть календарь
    browser.element('#dateOfBirthInput').click()

    # 2. Выбрать месяц (январь)
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').should(be.visible).click()

    # 3. Выбрать год (1991)
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1991"]').should(be.visible).click()

    # 4. Выбрать день (01)
    browser.element('.react-datepicker__day--001').click()

    # 5. Проверить результат
    browser.element('#dateOfBirthInput').should(have.value("01 Jan 1991"))

    # Выбор Subjects + проверка
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('.subjects-auto-complete__multi-value').should(have.text('Computer Science'))  # Проверка выбранного предмета

    # Выбор хобби + проверка
    browser.element("#submit").perform(command.js.scroll_into_view)
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#hobbies-checkbox-1').should(be.selected)

    # Загрузка файла
    browser.element('#uploadPicture').send_keys(image_path) # Проверка введенного значения

    # Заполнение адреса + проверка
    browser.element('#currentAddress').type("ул.Ленина д.3 кв.3")
    browser.element('#currentAddress').should(have.value("ул.Ленина д.3 кв.3"))

    # Выбор штата и города (проверка выбранных значений)
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#state .css-1uccc91-singleValue').should(have.text('Haryana'))  # Проверка выбранного штата

    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#city .css-1uccc91-singleValue').should(have.text('Karnal'))  # Проверка выбранного города

    # Отправка формы
    browser.element('#submit').click()