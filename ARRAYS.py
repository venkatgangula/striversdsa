       #                   ARRAY
       #                     │
       #                     ▼
       #             ┌───────────────┐
       #             │ CONSTRAINTS   │
       #             └───────┬───────┘
       #                     │
       #              ┌──────┴──────┐
       #              │             │
       #           small          large
       #              │             │
       #           brute         optimize
       #                            │
       #                            ▼
       #                   ┌────────────────┐
       #                   │ WHAT IS ASKED? │
       #                   └───────┬────────┘
       #                           │
       #      ┌────────────────────┼─────────────────────┐
       #      │                    │                     │
       #      ▼                    ▼                     ▼
       #   ELEMENT              SUBARRAY                PAIR
       #      │                    │                     │
       #      ▼                    ▼                     ▼
       #  Set/HashMap       Window / Prefix Sum      HashMap
       #                                               Pointer
       #      │                    │
       #      │           ┌────────┴────────┐
       #      │           │                 │
       #      │        Positive          Negative
       #      │           │                 │
       #      │           ▼                 ▼
       #      │       Window           Prefix Sum
       #      │
       #      ▼
       # DUPLICATE?
       #      │
       #      ▼
       #     SET

       #                     ↓
       #              SORTED ARRAY?
       #                     │
       #              ┌──────┴──────┐
       #              ▼             ▼
       #             YES            NO
       #              │             │
       #              ▼             ▼
       #        2 Pointer       HashMap/Sort
       #        Binary Search

       #                     ↓
       #              COMPLEXITY CHECK
       #                     │
       #              ┌──────┴──────┐
       #              ▼             ▼
       #           O(n²) ❌      O(n)/O(logn) ✅





