import time
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

selected_folder = None

def login_to_website():
    driver = webdriver.Chrome()
    driver.get('https://selpics.youfocus.com.br/login')
    email_field = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    password_field = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.vf.input input[type="password"]'))
    )
    email = email_entry.get()
    password = password_entry.get()
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(1)
    return driver

def web_scraping_after_login(driver, album_url, photos_directory):
    try:
        driver.get(album_url)
        time.sleep(1)
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, 'html.parser')
        elements_with_specific_class = soup.find_all(class_='vf filename font-13')
        names = []
        for element in elements_with_specific_class:
            name = element.text
            names.append(name)
        for name in names:
            print(name)
        source_directory = photos_directory
        destination_directory = os.path.join(photos_directory, 'Chosen')
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        for name in names:
            source_file = os.path.join(source_directory, name)
            destination_file = os.path.join(destination_directory, name)
            if os.path.exists(source_file):
                shutil.copy2(source_file, destination_file)
                selected_photos_listbox.insert(tk.END, name)
        selected_photos_listbox.insert(tk.END,
                                       'Selected photos have been copied to the "Chosen" folder successfully.')
    except Exception as e:
        print(f'Error accessing the page: {str(e)}')
    driver.quit()

def select_directory():
    global selected_folder
    folder_selected = filedialog.askdirectory()
    selected_folder = folder_selected.replace('/', '\\')
    photos_directory_entry.delete(0, tk.END)
    photos_directory_entry.insert(0, selected_folder)

root = tk.Tk()
root.title('Selpics Photo Extractor')
root.geometry('800x500')

custom_font = ('Helvetica', 12)

album_url_label = tk.Label(root, text='Album URL:', font=custom_font)
album_url_label.pack()
album_url_entry = tk.Entry(root, width=80, font=custom_font)
album_url_entry.pack()

photos_directory_label = tk.Label(root, text='Photo directory:', font=custom_font)
photos_directory_label.pack()
photos_directory_entry = tk.Entry(root, width=80, font=custom_font)
photos_directory_entry.pack()

select_directory_button = tk.Button(root, text='Select directory', command=select_directory, font=custom_font)
select_directory_button.pack()

blank_space = tk.Label(root, text='', font=custom_font)
blank_space.pack()

email_label = tk.Label(root, text='Email:', font=custom_font)
email_label.pack()
email_entry = tk.Entry(root, width=80, font=custom_font)
email_entry.pack()

password_label = tk.Label(root, text='Password:', font=custom_font)
password_label.pack()
password_entry = tk.Entry(root, width=80, show='*', font=custom_font)
password_entry.pack()

blank_space = tk.Label(root, text='', font=custom_font)
blank_space.pack()

start_button = tk.Button(root, text='Start', command=lambda: web_scraping_after_login(login_to_website(), album_url_entry.get(), selected_folder), font=custom_font)
start_button.pack()

selected_photos_listbox = tk.Listbox(root, width=80, height=10, font=custom_font)
selected_photos_listbox.pack()

success_label = tk.Label(root, text='', font=custom_font)
success_label.pack()

root.mainloop()