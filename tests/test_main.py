import unittest
from unittest.mock import patch, AsyncMock
import asyncio
import os

from main import get_all_cats, save_to_disk, main  # Импортируем функции из вашего основного файла


class TestCatFunctions(unittest.IsolatedAsyncioTestCase):

    @patch('main.aiohttp.ClientSession.get')
    async def test_get_all_cats_success(self, mock_get):
        # Создаем асинхронную мок-функцию
        mock_response = AsyncMock()
        mock_response.read.return_value = b'test'
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await get_all_cats()
        self.assertEqual(len(result), 10)  # Предположим, что должно быть загружено 10 котов

    def test_save_to_disk(self):
        # Создаем директорию, если ее нет
        if not os.path.exists('cats'):
            os.makedirs('cats')

        # Проверяем, сохраняется ли файл на диск
        content = b"test content"
        save_to_disk(content, 1)
        with open("cats/1.png", "rb") as f:
            self.assertEqual(f.read(), content)

        # Удаляем созданный файл
        os.remove("cats/1.png")

    def test_main_function(self):
        # Тестируем основную функцию
        main()
        self.assertTrue(True)  # Просто проверяем, что функция выполняется без ошибок

    @patch('main.aiohttp.ClientSession.get')
    async def test_get_all_cats_fail(self, mock_get):
        # Создаем асинхронную мок-функцию
        mock_response = AsyncMock()
        mock_response.read.return_value = b'test'
        mock_response.status = 404
        mock_get.return_value.__aenter__.return_value = mock_response

        with self.assertRaises(Exception):
            await get_all_cats('invalid_url')

    def test_save_to_disk_fail(self):
        # Тестируем случай неудачного сохранения файла
        content = b"test content"
        with self.assertRaises(Exception):
            save_to_disk(content, '/invalid/path/1.png')


if __name__ == '__main__':
    unittest.main()
