# 🚖 Ride-Sharing Dispatch Simulator

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) 
[![Status](https://img.shields.io/badge/status-active-success.svg)]()  

---

# 📌 Project Overview
The **Ride-Sharing Dispatch Simulator** is a Python-based system that mimics how platforms like Uber or Lyft assign drivers to riders.  
It focuses on **fair and efficient matching** by considering:  
- 🚗 **Distance** → Nearest driver gets priority  
- ⭐ **Driver rating** → Higher-rated drivers win ties  
- ⏱ **Availability order** → First available driver is chosen if distance & rating are equal  

This simulator uses fundamental data structures like **queues** and **priority queues** to model real-world ride-sharing behavior.  
It’s lightweight, dependency-free, and serves as a great project for learning about **algorithms, data structures, and simulations** in Python.  

---

# ✨ Features
✔ Queue (`deque`) for incoming ride requests (FIFO)  
✔ Priority queue (`heapq`) for nearest-driver selection  
✔ Tie-breakers: higher rating → availability order  
✔ Maintains full ride history (with fare & distance)  
✔ Lightweight, dependency-free (pure Python)  

---

# 🧠 Data Structures
### **Ride Request Queue**
> FIFO structure storing `RideRequest` objects  

### **Driver Heap**
> Ranked by:  
> - Distance (ascending)  
> - Rating (descending)  
> - Availability order (ascending)  

### **Dictionaries**
> Fast lookup of **drivers**, **riders**, and **rides**  

---

# 🧮 Matching Logic
1️⃣ **Take next ride request** from the queue  
2️⃣ **Build driver heap** from all available drivers  
3️⃣ **Select nearest driver** (apply tie-breakers)  
4️⃣ **Assign ride → Mark driver unavailable → Log ride**  

---

# 📦 Project Layout


ride\_sharing\_dispatch\_sim/
1. app.py          # Demo application
2. simulator.py    # Core classes and dispatch logic
3.README.md       # Documentation

`

---

# 🚀 Quick Start
Run the demo locally:

bash
python3 app.py
`

This will:
👉 Register drivers & riders
👉 Enqueue ride requests
👉 Dispatch requests to drivers
👉 Complete rides and print ride history

---

# 🧪 Example Output


Enqueued Request: rider=R1 -> drop=(8, 2)
Assigned: rider R1 -> driver D3 (dist=2.83, rating=4.9)
Ride completed: id=1, fare=₹68.00

Ride History:
Ride 1: Rider=R1, Driver=D3, Distance=8.06, Fare=₹68.00


---

# 🧩 Extending the Simulator

🔹 Real-time driver location updates
🔹 Surge pricing and ETA calculation
🔹 Ride cancellations & timeouts
🔹 Smarter spatial indexing (Geo-hash, KD-Tree)
🔹 Persistent history storage (e.g., SQLite)
🔹 Async or concurrent request handling

---

# ⚙️ Requirements

* **Python 3.9+**
* Uses only standard library modules: `dataclasses`, `collections`, `heapq`, `time`, `math`

---

# 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
✔ Free to use, modify, and distribute with attribution.
✔ No liability for issues arising from use.

---

# 📊 Status

🟢 **Active** → This project is being maintained and improved.

