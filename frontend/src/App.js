import { Outlet, Link } from "react-router-dom";
import Footer from "./Footer";

export default function App() {
  return (
    <div>
      <h1 className="text-3xl font-bold underline">Chat History Analyzer</h1>
      <nav
        style={{
          borderBottom: "solid 1px",
          paddingBottom: "1rem",
        }}
      >
        <Link to="/invoices">Invoices</Link> |{" "}
        <Link to="/expenses">Expenses</Link>
      </nav>
      <Outlet />
      <Footer />
    </div>
  );
}
