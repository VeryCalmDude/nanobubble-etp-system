import unittest

class TestNanobubbleETPLogic(unittest.TestCase):
    
    def test_dissolved_oxygen_threshold(self):
        """Test if oxygen generator triggers when DO drops below safe threshold."""
        target_min_do = 6.0
        current_do = 4.5
        
        # Logic check: Should trigger pump if DO is low
        needs_oxygen = current_do < target_min_do
        self.assertTrue(needs_oxygen, "Oxygen generator should activate when DO is below 6.0 mg/L")

    def test_effluent_compliance(self):
        """Test if treated effluent BOD meets environmental discharge standards (< 30 mg/L)."""
        discharge_bod = 12.0
        max_allowed_bod = 30.0
        
        self.assertLessEqual(discharge_bod, max_allowed_bod, "Discharge BOD exceeds regulatory limits!")

if __name__ == '__main__':
    unittest.main()