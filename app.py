from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok", "service": "hotel-booking"}

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StayEase | Hotel Booking</title>

<style>
:root {
  --bg: #0f172a;
  --card: rgba(255,255,255,0.06);
  --border: rgba(255,255,255,0.1);
  --accent: #6366f1;
  --accent2: #22d3ee;
  --text: #f1f5f9;
  --muted: #94a3b8;
}

body {
  margin:0;
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(135deg,#020617,#0f172a);
  color: var(--text);
}

.container {
  max-width: 1200px;
  margin:auto;
  padding:20px;
}

.header {
  display:flex;
  justify-content:space-between;
  align-items:center;
}

.logo {
  font-size:22px;
  font-weight:bold;
}

.hero {
  margin-top:30px;
  padding:40px;
  border-radius:20px;
  background: linear-gradient(135deg,#6366f144,#22d3ee22);
  border:1px solid var(--border);
}

.hero h1 {
  margin:0;
  font-size:42px;
}

.grid {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:20px;
  margin-top:30px;
}

.card {
  background:var(--card);
  border:1px solid var(--border);
  border-radius:20px;
  overflow:hidden;
  transition:0.3s;
}

.card:hover {
  transform:translateY(-5px);
}

.card img {
  width:100%;
  height:180px;
  object-fit:cover;
}

.card-body {
  padding:15px;
}

.price {
  font-size:20px;
  font-weight:bold;
}

button {
  width:100%;
  margin-top:10px;
  padding:10px;
  border:none;
  border-radius:10px;
  background: linear-gradient(135deg,var(--accent),var(--accent2));
  color:white;
  cursor:pointer;
}

.booking {
  margin-top:30px;
  padding:20px;
  border-radius:20px;
  border:1px solid var(--border);
}

input, select {
  width:100%;
  padding:10px;
  margin-top:10px;
  border-radius:10px;
  border:none;
}

.summary {
  margin-top:20px;
  padding:15px;
  border-radius:15px;
  background:var(--card);
}
</style>
</head>

<body>

<div class="container">

<div class="header">
  <div class="logo">🏨 StayEase</div>
  <div>Easy Hotel Booking</div>
</div>

<div class="hero">
  <h1>Find your perfect stay</h1>
  <p>Book hotels easily with a clean and modern experience.</p>
</div>

<div class="grid" id="hotelList"></div>

<div class="booking">
  <h2>Booking Panel</h2>

  <label>Selected Hotel</label>
  <input id="hotelName" readonly>

  <label>Check-in Date</label>
  <input type="date" id="checkin">

  <label>Check-out Date</label>
  <input type="date" id="checkout">

  <label>Guests</label>
  <select id="guests">
    <option>1</option>
    <option>2</option>
    <option>3</option>
  </select>

  <div class="summary">
    <p>Price per night: <span id="price">₹0</span></p>
    <p>Total: <span id="total">₹0</span></p>
  </div>

  <button onclick="book()">Book Now</button>
</div>

</div>

<script>
const hotels = [
  {name:"Ocean View Resort", price:4000, img:"https://images.unsplash.com/photo-1501117716987-c8e1ecb210c1"},
  {name:"Mountain Retreat", price:3500, img:"https://images.unsplash.com/photo-1505691938895-1758d7feb511"},
  {name:"City Luxury Hotel", price:5000, img:"https://images.unsplash.com/photo-1566073771259-6a8506099945"}
];

let selectedPrice = 0;

const list = document.getElementById("hotelList");

hotels.forEach(h => {
  list.innerHTML += `
    <div class="card">
      <img src="${h.img}">
      <div class="card-body">
        <h3>${h.name}</h3>
        <div class="price">₹${h.price}</div>
        <button onclick="selectHotel('${h.name}',${h.price})">Select</button>
      </div>
    </div>
  `;
});

function selectHotel(name, price) {
  document.getElementById("hotelName").value = name;
  document.getElementById("price").innerText = "₹" + price;
  selectedPrice = price;
  calculate();
}

document.getElementById("checkin").addEventListener("change", calculate);
document.getElementById("checkout").addEventListener("change", calculate);

function calculate() {
  let inDate = new Date(document.getElementById("checkin").value);
  let outDate = new Date(document.getElementById("checkout").value);

  if (!inDate || !outDate) return;

  let nights = (outDate - inDate) / (1000*60*60*24);
  if (nights > 0) {
    document.getElementById("total").innerText = "₹" + (nights * selectedPrice);
  }
}

function book() {
  if (!document.getElementById("hotelName").value) {
    alert("Select hotel first");
    return;
  }
  alert("Booking Confirmed 🎉");
}
</script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
