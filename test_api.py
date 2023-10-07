import unittest
import json
# TODO: separate 
from fastapi.testclient import TestClient
from main import app, CONST_DEFAULT_MSG

test_item = {
            "name": "Bananenshake",
            "description": "Banana Shake Coffee",
            "price": 10.0,
            "tax": 19.0,
            "total_price": 11.9,
            "amount":0
        }

class TestDependencies(unittest.TestCase):
    def testUnitTest(self):
        self.assertEqual(1,1,"Unit Tests funktionieren nicht")
    def testHaveJSON(self):
        import json
    def testHaveFastAPI(self):
        import fastapi
    def testHaveTestClient(self):
        import fastapi.testclient
        return
    def testHaveUvicorn(self):
        import uvicorn
        return
    def testFoundMainModule(self):
        import main

class TestAPIRoutes(unittest.TestCase):
    def testRoute(self):
        client = TestClient(app)
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), CONST_DEFAULT_MSG)
    
    def testGetItemsEmpty(self):
        client = TestClient(app)
        response = client.get("/items")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), [])

    def testPostItem(self):
        client = TestClient(app)
        response = client.post("/item", json=test_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), test_item)

    def testPostAndGetItems(self):
        client = TestClient(app)
        response = client.post("/item", json=test_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), test_item)
        response = client.get("/items")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), [test_item])

    def testPostAndClearItems(self):
        client = TestClient(app)
        response = client.post("/item", json=test_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), test_item)
        response = client.get("/clear-items")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), [])
    

if __name__ == "__main__":
    unittest.main()
