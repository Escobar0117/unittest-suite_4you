import re
from playwright.sync_api import Page, expect

#pytest --slowmo 1500  --headed  test_dos.py 

def test_dos(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("ToolsQA")
    
    #boton uno
    #boton_uno=page.locator("text=Elements").click()
    page.locator("text=Elements").click()
    page.screenshot(path="Imagenes/boton_uno_click.png")
    # page.screenshot(path="Imagenes/boton_uno.png")
    # boton_uno.click()
    # page.screenshot(path="Imagenes/boton_uno_click.png")
    #ctrl + }
    #Validar la Url
    expect(page).to_have_url(re.compile(".*elements"))
    
    page.locator("text=Text Box").click()
    page.screenshot(path="Imagenes/boton_dos_click.png")
    expect(page).to_have_url(re.compile(".*text-box"))
    
    #Primer texto campo nombre
    #page.locator("#userName").fill("Rodrigo")
    page.locator("//input[@id='userName']").fill("Rodrigo")    
    page.screenshot(path="Imagenes/texto_nombre.png")
    
    page.locator("//input[@id='userEmail']").fill("rodrigo@gmail.com")    
    page.screenshot(path="Imagenes/texto_email.png")
    
    page.locator("#currentAddress").fill("Dirección uno demo")    
    page.screenshot(path="Imagenes/texto_dirección.png")
    
    page.locator("//textarea[@id='permanentAddress']").fill("Dirección dos permanente demo")    
    page.screenshot(path="Imagenes/texto_dirección2.png")
    
    page.locator("//button[@id='submit']").click()
    page.screenshot(path="Imagenes/boton_Cargar.png")
    
    expect(page).to_have_url(re.compile(".*text-box"))
    
    
    
    
    
    
    
    
   