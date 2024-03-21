import flet as ft
import subprocess


def execute_script(e):
    subprocess.run(["python", "organize.py"])
    # show result
    result_text.value = "Organization has finished!"
    # update the page
    e.page.update()


def main(page: ft.Page):
    page.title = "Organize Script"
    page.font_family = "Khula"  # Khulaフォントを設定
    page.window_height = 200
    page.window_width = 300

    # buttuon
    execute_button = ft.OutlinedButton("Execute", on_click=execute_script)

    # instruction text
    instruction_text = ft.Text("Click the button to organize your files")

    # show result
    global result_text
    result_text = ft.TextField(value="", disabled=True, width=300)

    # pack
    page.add(instruction_text, execute_button, result_text)


if __name__ == "__main__":
    ft.app(target=main)
