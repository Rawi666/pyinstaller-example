"""
Simple demonstration application for PyInstaller.

This app demonstrates basic functionality with external dependencies
that can be packaged into a standalone executable.
"""

from datetime import datetime
from colorama import Fore, Style, init
from dateutil import parser, relativedelta
import platform


def display_welcome() -> None:
    """Display a colorful welcome message."""
    init(autoreset=True)  # Initialize colorama
    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.YELLOW}  PyInstaller Demo Application")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}\n")


def display_system_info() -> None:
    """Display basic system information to show the app is working."""
    current_time = datetime.now()

    # Use python-dateutil to calculate relative time
    future_date = current_time + relativedelta.relativedelta(months=6, days=15)

    print(f"{Fore.GREEN}System:{Style.RESET_ALL} {platform.system()} {platform.release()}")
    print(f"{Fore.GREEN}Current Time:{Style.RESET_ALL} {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{Fore.GREEN}Future Date (+6 months, 15 days):{Style.RESET_ALL} {future_date.strftime('%Y-%m-%d')}")
    print(f"\n{Fore.CYAN}Third-Party Dependencies Loaded:{Style.RESET_ALL}")
    print("  ✓ colorama (colored terminal output)")
    print("  ✓ python-dateutil (advanced date/time handling)")
    print()


def demonstrate_date_operations() -> None:
    """Demonstrate python-dateutil functionality."""
    print(f"{Fore.YELLOW}Date Parsing Demo (python-dateutil):{Style.RESET_ALL}")

    # Parse a date string
    sample_date_string = "2025-12-25"
    parsed_date = parser.parse(sample_date_string)
    days_until = (parsed_date - datetime.now()).days

    print(f"  String: '{sample_date_string}'")
    print(f"  Parsed: {parsed_date.strftime('%B %d, %Y')}")
    print(f"  Days from now: {days_until} days")
    print()


def main() -> None:
    """
    Main application entry point.

    Displays a welcome message, system info, and demonstrates the bundled dependencies.
    """
    display_welcome()
    display_system_info()
    demonstrate_date_operations()

    print(f"{Fore.GREEN}✓ All dependencies working correctly!{Style.RESET_ALL}")
    print()


if __name__ == "__main__":
    main()
