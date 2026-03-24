import re
from playwright.sync_api import Page, Locator, expect

from testing.pages.config import (
    formulario_email,
    formulario_telefono,
    formulario_mensaje,
    formulario_nombre,
    url_que_es_4you,
)


class FormularioContactanos:
    def __init__(self, page: Page):
        self.page = page

        # Selectores originales (sin modificar xpath)
        self.title_main_selector = "text=Cuida lo que mas valoras"
        self.btn_contactanos_selector = "(//span[@class='FyLandingButtons-module__4AF9HG__label'][normalize-space()='Contactanos'])[1]"
        self.input_name_selector = "//input[@id='fy-name']"
        self.input_email_selector = "//input[@id='fy-email']"
        self.input_phone_selector = "//input[@id='fy-phone']"
        self.input_message_selector = "//textarea[@class='form-control is-invalid']"
        self.btn_submit_selector = "//span[normalize-space()='Submit']"
        self.form_container_selector = "//form"

        # Locators
        self.title_main: Locator = self.page.locator(self.title_main_selector)
        self.btn_contactanos: Locator = self.page.locator(self.btn_contactanos_selector)
        self.input_name: Locator = self.page.locator(self.input_name_selector)
        self.input_email: Locator = self.page.locator(self.input_email_selector)
        self.input_phone: Locator = self.page.locator(self.input_phone_selector)
        self.input_message: Locator = self.page.locator(self.input_message_selector)
        self.btn_submit: Locator = self.page.locator(self.btn_submit_selector)
        self.form_container: Locator = self.page.locator(self.form_container_selector)

    def navigate(self) -> None:
        """Navega a la página principal y valida que cargó correctamente."""
        self.page.goto(url_que_es_4you, wait_until="domcontentloaded")
        expect(self.title_main).to_be_visible()

    def click_contactanos(self) -> None:
        """Hace clic en el botón 'Contactanos' y valida redirección al formulario."""
        expect(self.btn_contactanos).to_be_visible()
        expect(self.btn_contactanos).to_be_enabled()
        self.btn_contactanos.click()

        expect(self.form_container).to_be_visible()
        expect(self.page).to_have_url(re.compile(".*bienvenida"))

    def fill_form(
        self,
        nombre: str = formulario_nombre,
        email: str = formulario_email,
        telefono: str = formulario_telefono,
        mensaje: str = formulario_mensaje,
    ) -> None:
        """Llena el formulario de contacto."""
        expect(self.input_name).to_be_visible()
        expect(self.input_email).to_be_visible()
        expect(self.input_phone).to_be_visible()
        expect(self.input_message).to_be_visible()

        self.input_name.fill(nombre)
        self.input_email.fill(email)
        self.input_phone.fill(telefono)
        self.input_message.fill(mensaje)

    def submit_form(self) -> None:
        """Envía el formulario."""
        expect(self.btn_submit).to_be_visible()
        expect(self.btn_submit).to_be_enabled()
        self.btn_submit.click()

    def complete_contact_form(
        self,
        nombre: str = formulario_nombre,
        email: str = formulario_email,
        telefono: str = formulario_telefono,
        mensaje: str = formulario_mensaje,
    ) -> None:
        """Ejecuta el flujo completo del formulario."""
        self.navigate()
        self.click_contactanos()
        self.fill_form(nombre, email, telefono, mensaje)
        self.submit_form()