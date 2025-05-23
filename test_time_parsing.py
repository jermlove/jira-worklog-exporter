#!/usr/bin/env python3

from exporter import parse_time_spent, format_minutes_to_hhmm

def test_time_parsing():
    """Test the time parsing function with various formats"""
    
    test_cases = [
        ("1d", 8 * 60),      # 1 day = 8 hours = 480 minutes
        ("2w", 80 * 60),     # 2 weeks = 10 days = 80 hours = 4800 minutes  
        ("1h", 60),          # 1 hour = 60 minutes
        ("30m", 30),         # 30 minutes
        ("1h 30m", 90),      # 1 hour 30 minutes = 90 minutes
        ("1d 2h", 10 * 60),  # 1 day + 2 hours = 10 hours = 600 minutes
        ("1w 1d", 48 * 60),  # 1 week + 1 day = 6 days = 48 hours = 2880 minutes
    ]
    
    print("Testing time parsing function:")
    print("=" * 50)
    
    for time_str, expected_minutes in test_cases:
        result_minutes = parse_time_spent(time_str)
        result_formatted = format_minutes_to_hhmm(result_minutes)
        expected_formatted = format_minutes_to_hhmm(expected_minutes)
        
        status = "✅ PASS" if result_minutes == expected_minutes else "❌ FAIL"
        
        print(f"{status} | {time_str:8} -> {result_formatted:12} (expected: {expected_formatted})")
        
        if result_minutes != expected_minutes:
            print(f"      Expected {expected_minutes} minutes, got {result_minutes} minutes")
    
    print("\n" + "=" * 50)
    
    # Test with your actual data
    print("Testing with your actual worklog data:")
    actual_entries = ["1d", "2w"]
    total_minutes = 0
    
    for entry in actual_entries:
        minutes = parse_time_spent(entry)
        total_minutes += minutes
        formatted = format_minutes_to_hhmm(minutes)
        print(f"  {entry:3} = {formatted}")
    
    total_formatted = format_minutes_to_hhmm(total_minutes)
    print(f"\nTotal: {total_formatted}")
    print(f"(This should be 88 hrs 0 min, not 8 hrs 0 min)")

if __name__ == "__main__":
    test_time_parsing()
