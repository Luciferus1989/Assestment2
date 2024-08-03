import unittest
from unittest.mock import patch, AsyncMock
import os

from main import get_all_cats, save_to_disk, main


class TestCatFunctions(unittest.IsolatedAsyncioTestCase):

    @patch('main.aiohttp.ClientSession.get')
    async def test_get_all_cats_success(self, mock_get):

        mock_response = AsyncMock()
        mock_response.read.return_value = b'test'
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await get_all_cats()
        self.assertEqual(len(result), 10)

    def test_save_to_disk(self):
        if not os.path.exists('cats'):
            os.makedirs('cats')
        content = b"test content"
        save_to_disk(content, 1)
        with open("cats/1.png", "rb") as f:
            self.assertEqual(f.read(), content)
        os.remove("cats/1.png")

    def test_main_function(self):
        main()
        self.assertTrue(True)

    @patch('main.aiohttp.ClientSession.get')
    async def test_get_all_cats_fail(self, mock_get):
        mock_response = AsyncMock()
        mock_response.read.return_value = b'test'
        mock_response.status = 404
        mock_get.return_value.__aenter__.return_value = mock_response

        with self.assertRaises(Exception):
            await get_all_cats('invalid_url')

    def test_save_to_disk_fail(self):
        content = b"test content"
        with self.assertRaises(Exception):
            save_to_disk(content, '/invalid/path/1.png')


if __name__ == '__main__':
    unittest.main()
