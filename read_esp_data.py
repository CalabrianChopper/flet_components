import flet as ft
import asyncio
import aiohttp
import json

BASE_URL = "http://192.168.4.1"

async def get_sensor_data(session):
    async with session.get(f"{BASE_URL}/GET/get_sensor_data") as response:
        return await response.json()

async def set_pause_duration(session, new_duration):
    async with session.get(f"{BASE_URL}/SET/set_pause_duration?pause={new_duration}") as response:
        return await response.text()

async def update_pause_duration(session, change, current_duration, page):
    new_duration = max(1, current_duration + change)  # Assicura che la durata non sia mai inferiore a 1
    result = await set_pause_duration(session, new_duration)
    if "successo" in result:
        page.data['pause_duration'] = new_duration
        await update_data(page, session)
    else:
        print(f"Errore nell'aggiornamento della durata della pausa: {result}")

async def update_data(page, session):
    try:
        data = await get_sensor_data(session)
        
        page.data['pause_duration'] = data['pause_duration']
        
        page.controls[0].controls = [
            ft.Text(f"Temperatura: {data['temperature']}°C"),
            ft.Text(f"Umidità: {data['humidity']}%"),
            ft.Text(f"Stato pompa: {'Accesa' if data['pump_state'] == 1 else 'Spenta'}"),
            ft.Text(f"Durata ciclo pompa: {data['pump_duration']} minuti"),
            ft.Text(f"Durata pausa: {data['pause_duration']} minuti"),
            ft.Text(f"Riavvio tra: {data['restart_counter']} cicli")
        ]
        page.update()
    except Exception as e:
        print(f"Errore durante l'aggiornamento dei dati: {e}")

async def main(page: ft.Page):
    page.title = "Controllo Pompa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.data = {'pause_duration': 1}  # Valore di default

    data_container = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    
    async def on_button_click(e, change):
        async with aiohttp.ClientSession() as session:
            await update_pause_duration(session, change, page.data['pause_duration'], page)

    buttons_row = ft.Row([
        ft.ElevatedButton("-10", on_click=lambda _: asyncio.create_task(on_button_click(_, -10))),
        ft.ElevatedButton("-1", on_click=lambda _: asyncio.create_task(on_button_click(_, -1))),
        ft.ElevatedButton("+1", on_click=lambda _: asyncio.create_task(on_button_click(_, 1))),
        ft.ElevatedButton("+10", on_click=lambda _: asyncio.create_task(on_button_click(_, 10))),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(data_container, buttons_row)

    async def periodic_update():
        async with aiohttp.ClientSession() as session:
            while True:
                await update_data(page, session)
                await asyncio.sleep(10)

    asyncio.create_task(periodic_update())

ft.app(target=main)