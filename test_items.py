link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_open_store_link_see_button(browser):
	browser.get(link)
	#проверка наличия кнопки добавить в корзину по селектору
	assert browser.find_elements_by_css_selector(".btn-add-to-basket"), 'Миша, все фигня, начинай сначала'