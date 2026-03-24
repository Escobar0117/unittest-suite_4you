from playwright.sync_api import Page

from testing.pages.que_es_4you.formulario_contactanos import FormularioContactanos


def test_formulario_contactanos(page: Page):
    form = FormularioContactanos(page)

    form.navigate()
    form.click_contactanos()
    form.fill_form()
    form.submit_form()