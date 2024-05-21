import flet as ft 

def home(url):
    text = ft.Text("Messenger")
    
    
    chat = ft.Column()
    
    def send_msg_tunnel(info):
        chat.controls.append(info)
        url.update()
    
    url.pubsub.subscribe(send_msg_tunnel)
    
    def send_msg(event):
        text = ft.Text(f'{username.value}: {campo_msg.value}')
        url.pubsub.send_all(text)
        campo_msg.value = ''
        url.update()
        
    campo_msg = ft.TextField(label='Escreva sua mensagem:', on_submit=send_msg)
    send_btn = ft.ElevatedButton('Enviar', on_click=send_msg)
    
    def enter_chat(event):
        popup.open = False
        url.remove(start_btn)
        url.add(chat)
        linha_msg = ft.Row(
            [campo_msg,
            send_btn]
        )
        url.add(linha_msg)
        text = ft.Text(f'{username.value} entrou.')
        url.pubsub.send_all(text)
        url.update()
    
    
    username = ft.TextField(label='Nome:', on_submit=enter_chat)
    
    def cancel(event):
        popup.open = False
        username.value = ''
        url.update()
        
    
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Messenger'),
        content=username,
        actions=[ft.ElevatedButton('Cancelar', on_click=cancel),ft.ElevatedButton('Ok', on_click=enter_chat)]
        )
    
    def start_chat(event):
        url.dialog = popup
        popup.open = True
        url.update()
        
    start_btn = ft.ElevatedButton('Start', on_click=start_chat)
    
    
    
    url.add(text)
    url.add(start_btn)

ft.app(home, view=ft.WEB_BROWSER)