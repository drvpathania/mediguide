import { Link } from "react-router-dom";

export default function Home() {
  const phone = "919811387746";

  return (
    <div style={{ textAlign: "center", padding: 20 }}>

      {/* HERO */}
      <h1>Dr Vishal Pathania</h1>
      <h2>ENT Specialist in Gurgaon</h2>

      <p>Ear • Nose • Throat • Sinus • Hearing • Thyroid</p>

      <div>
        <a href={`https://wa.me/${phone}?text=I want appointment`}>
          <button>📲 WhatsApp Now</button>
        </a>

        <button onClick={() => window.scrollTo(0, 600)}>
          📅 Book Appointment
        </button>
      </div>

      <p>⭐ 4.9 Rating | 895+ Patients</p>

      {/* SERVICES */}
      <h3>Services</h3>
      <ul>
        <li>Ear Pain</li>
        <li>Sinus</li>
        <li>Hearing Loss</li>
        <li>Vertigo</li>
        <li>Tonsillitis</li>
        <li>Thyroid</li>
      </ul>

      {/* AI FEATURE */}
      <h3>Check Symptoms (AI)</h3>
      <p>Get instant ENT advice</p>
      <Link to="/ai">
        <button>🤖 Use AI Assistant</button>
      </Link>

      {/* BOOKING */}
      <h3 id="booking">Book Appointment</h3>
      <input placeholder="Name" /><br/>
      <input placeholder="Age" /><br/>
      <input placeholder="Phone" /><br/>
      <textarea placeholder="Symptoms" /><br/>

      <button>Submit</button>

      {/* LOCATION */}
      <h3>Visit Clinic</h3>
      <p>Sector 49, Gurgaon</p>

      {/* FLOATING WHATSAPP */}
      <a
        href={`https://wa.me/${phone}`}
        style={{
          position: "fixed",
          bottom: 20,
          right: 20,
          background: "green",
          color: "white",
          padding: 15,
          borderRadius: "50%"
        }}
      >
        💬
      </a>

    </div>
  );
}