"""Utility functions for the Student Management System."""


def highest_score(data):
    """Return the student dict with the highest score."""
    if not data:
        return None
    return max(data, key=lambda d: d["score"])


def lowest_score(data):
    """Return the student dict with the lowest score."""
    if not data:
        return None
    return min(data, key=lambda d: d["score"])

def highest_stock_item(data):
    """Return the inventory item with the highest quantity."""
    if not data:
        return None
    return max(data, key=lambda d: d["quantity"])


def lowest_stock_item(data):
    """Return the inventory item with the lowest quantity."""
    if not data:
        return None
    return min(data, key=lambda d: d["quantity"])