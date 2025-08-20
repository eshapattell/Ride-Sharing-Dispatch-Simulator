# 🚖 Ride-Sharing-Dispatch-Simulator

Assign drivers to riders based on **distance first**, then **rating** — using a **queue** for incoming ride requests and a **priority queue (min-heap)** to pick the best driver for each request.

---

## ✨ Features
- **Queues**: `collections.deque` stores *incoming ride requests* FIFO.
- **Priority queues**: `heapq` ranks available drivers by *(distance, -rating, time_added)* for each request.
- **Nearest driver wins** (Euclidean distance). Ties go to higher driver rating, then FIFO order of driver availability.
- **Ride history**: every completed (and failed) dispatch is recorded with rider, driver, distance, and fare.
- **Tiny, pure-Python** (no external deps). Clear separation between core logic and a small demo app.

---

## 🧠 Data Structures
- **Request Queue**: FIFO of `RideRequest`.
- **Per-request Driver Heap**: `(distance, -rating, available_seq, driver_id)` for all currently-available drivers.
- **Dictionaries** for fast lookup of riders, drivers, rides.

---

## 🧮 Matching Logic (O(D log D) per request)
1. Pop the next `RideRequest` from the queue.  
2. Build a driver heap from all *available* drivers, keyed by computed distance to the pickup.  
3. Pop the top candidate → assign ride; mark driver unavailable.  
4. Log `Ride` and append to history.  

---

## 📦 Project Layout


ride\_sharing\_dispatch\_sim/
├── app.py          # Small CLI/demo that enqueues requests and processes them
├── simulator.py    # Core classes: Driver, Rider, RideRequest, Ride, DispatchSystem
└── README.md       # This file

`

---

## 🚀 Quick Start
bash
python3 app.py
`

You’ll see a short demo: drivers/riders added, requests enqueued, dispatches assigned nearest-first with rating tie-breaks, rides completed, and history printed.

---

## 🧪 Example Output (abridged)


Enqueued Request: rider=R1 -> drop=(8, 2)
Assigned: rider R1 -> driver D3 (dist=2.83, rating=4.9)
Ride completed: id=1, fare=₹68.00
...
Ride History (most recent last):
1) R1 with D3 distance=8.06 fare=₹68.00


---

## 🧩 Extending the Simulator

* Live driver location updates; periodic recompute or lazy update on assignment.
* Surge pricing and estimated time of arrival (ETA).
* Cancellations & timeouts (stale requests).
* Geo-hash buckets or KD-trees for sub-linear nearest-driver lookup.
* Persistent storage (SQLite/CSV) for history.
* Concurrency (asyncio, threads) if you want realism.

---

## ⚙️ Python Version

Python **3.9+** (uses `dataclasses` and type hints).

---

## 📄 License

MIT



👉 This version keeps the emojis ✅ but makes all headings *second-level (##), so they’re **larger and bolder* compared to the earlier smaller ones.  

Do you also want me to make the *section dividers (---) colorful with badges/icons* (like GitHub shields), or keep them plain and simple?
