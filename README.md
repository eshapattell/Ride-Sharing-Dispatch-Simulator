# 🚖 Ride-Sharing Dispatch Simulator

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) 
[![Status](https://img.shields.io/badge/status-active-success.svg)]()  

---

# 📌 Project Overview
The *Ride-Sharing Dispatch Simulator* is a Python-based project that simulates how ride-hailing platforms (like Uber, Lyft, or Ola) assign drivers to riders. The goal is to demonstrate the use of *queues, priority queues, and ride history management* through a realistic problem statement.  

In this simulator, whenever a new ride request is generated, the system identifies and assigns the *nearest available driver* to the rider. If multiple drivers are equally close, the assignment is determined using *driver ratings* as a tie-breaker, ensuring that both proximity and service quality are taken into account.  

The project maintains separate data structures for *available drivers, **waiting riders, and **completed ride history. Queues and priority queues are used strategically to make the assignment process efficient and fair. For example, riders waiting in line are handled using a **FIFO queue, while driver assignments are made with a **priority queue* based on distance and ratings.  

This project is not only a fun simulation of how modern ride-sharing apps function but also a practical demonstration of *Data Structures and Algorithms (DSA)* concepts like queues, heaps, and linked lists, along with object-oriented design.  

In short:  
- 🚕 Simulates real-world *ride-sharing dispatch systems*  
- 🧠 Reinforces *priority queues and queue operations*  
- 📊 Maintains *ride history* for future analysis  
- 🔄 Demonstrates real-time *driver-to-rider assignment logic*  
- 🎓 Great project for students learning *data structures* in Python

---

# ✨ Features

✔ *Driver–Rider Matching*  
Automatically assigns the nearest available driver to each rider. If two or more drivers are at the same distance, the driver with the *higher rating* is selected — ensuring both efficiency and quality.  

✔ *Queue Management for Riders*  
If no drivers are available, incoming riders are placed in a *waiting queue* (FIFO). As soon as a driver becomes free, the system assigns them to the next waiting rider.  

✔ *Priority Queue for Drivers*  
Drivers are organized using a *priority queue* based on distance and ratings, allowing the system to quickly identify the best driver for each request.  

✔ *Ride History Tracking*  
Every completed ride is recorded with details of the driver, rider, distance, and outcome. This history can be reviewed for analysis, debugging, or reporting purposes.  

✔ *Dynamic Updates*  
Drivers can become available or unavailable at any time. The system updates its data structures in real-time to reflect the changes.  

✔ *Scalable Design*  
Built with *object-oriented programming (OOP)* principles, making it easy to expand the simulator with additional features (like pricing, surge logic, or cancellation policies).  

✔ *Educational Value*  
Demonstrates practical use of:  
- *Queues* (for managing riders waiting in line)  
- *Priority Queues/Heaps* (for best driver selection)  
- *Linked Data Structures* (for ride history management)  

✔ *Lightweight & Simple*  
Runs entirely on *Python 3.9+* without any external dependencies. Easy to set up and experiment with.  

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

