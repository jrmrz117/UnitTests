import unittest

class TestStockVisualizer(unittest.TestCase):

    def setUp(self):
        self.stock_visualizer = StockVisualizer()

    def testSymbol(self):
        self.assertTrue(self.stock_visualizer.validateSymbol("AAPL"))
        self.assertTrue(self.stock_visualizer.validateSymbol("GOOG"))
        self.assertTrue(self.stock_visualizer.validateSymbol("MSFT"))
        self.assertFalse(self.stock_visualizer.validateSymbol("abcde"))
        self.assertFalse(self.stock_visualizer.validateSymbol("ABCD123"))
        self.assertFalse(self.stock_visualizer.validateSymbol("abcdefghi"))

    def testChartType(self):
        self.assertTrue(self.stock_visualizer.validateChartType("1"))
        self.assertTrue(self.stock_visualizer.validateChartType("2"))
        self.assertFalse(self.stock_visualizer.validateChartType("3"))
        self.assertFalse(self.stock_visualizer.validateChartType("O"))
        self.assertFalse(self.stock_visualizer.validateChartType("A"))

    def testTimeSeries(self):
        self.assertTrue(self.stock_visualizer.validateTimeSeries("1"))
        self.assertTrue(self.stock_visualizer.validateTimeSeries("2"))
        self.assertTrue(self.stock_visualizer.validateTimeSeries("3"))
        self.assertTrue(self.stock_visualizer.validateTimeSeries("4"))
        self.assertFalse(self.stock_visualizer.validateTimeSeries("5"))
        self.assertFalse(self.stock_visualizer.validateTimeSeries("O"))
        self.assertFalse(self.stock_visualizer.validateTimeSeries("A"))

    def testStartDate(self):
        self.assertTrue(self.stock_visualizer.validateStartDate("2022-01-01"))
        self.assertTrue(self.stock_visualizer.validateStartDate("2023-04-20"))
        self.assertFalse(self.stock_visualizer.validateStartDate("01-01-2022"))
        self.assertFalse(self.stock_visualizer.validateStartDate("2022/01/01"))
        self.assertFalse(self.stock_visualizer.validateStartDate("2022-13-01"))

    def testEndDate(self):
        self.assertTrue(self.stock_visualizer.validateEndDate("2022-01-01"))
        self.assertTrue(self.stock_visualizer.validateEndDate("2023-04-20"))
        self.assertFalse(self.stock_visualizer.validateEndDate("01-01-2022"))
        self.assertFalse(self.stock_visualizer.validateEndDate("2022/01/01"))
        self.assertFalse(self.stock_visualizer.validateEndDate("2022-13-01"))

if __name__ == '__main__':
    unittest.main()

        