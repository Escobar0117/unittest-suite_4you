from abc import ABC, abstractmethod

class Test(ABC):

    #Clase abstracta para login 4You

    def __init__(self, page):

        # Inicializa Playwright dentro de su clase
        self.setup_page(page)
        # Navegar al login
        self.page.goto("https://mi-app.com/login")
        self.is_login_successful = False

    def fill_username(self, username):
        self.page.locator("//input[@id='fy-email']").wait_for()
        self.page.locator("//input[@id='fy-email']").fill(username)

    def fill_password(self, password):
        self.page.locator("//input[@id='fy-password']").wait_for()
        self.page.locator("//input[@id='fy-password']").fill(password)

    def click_submit_button(self):
        self.page.locator("//button[contains(.,'Iniciar sesión')]").wait_for()
        self.page.locator("//button[contains(.,'Iniciar sesión')]").click()

    def verify_login_successful(self):
        try:
            self.page.locator("//div[@class='content-header-blue']").wait_for()
            self.page.locator("//button[@class='btn-menu-header']").wait_for()
            self.page.locator("//div[@class='caja-inicio-options-header']//a//img").wait_for()
            self.page.locator("//input[@type='search' and @placeholder='Buscar ...']").wait_for()
            self.page.locator("//h4[normalize-space()='Boletin']").wait_for()
            self.page.locator("//h4[normalize-space()='Comunicados']").wait_for()
            self.page.locator("//h4[normalize-space()='Aplicaciones más usadas']").wait_for()
            self.page.locator("//h4[normalize-space()='Últimos Documentos']").wait_for()
            self.page.locator("//h3[normalize-space()='Cumpleaños']").wait_for()

            self.is_login_successful = True
            return True

        except Exception as e:
            print(f"Error en login: {e}")
            self.page.screenshot(path="Error.png")
            return False

    def get_login_successful(self):
        return self.is_login_successful

    @abstractmethod
    def test(self):
        pass