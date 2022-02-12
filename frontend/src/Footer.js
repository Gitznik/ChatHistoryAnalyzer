import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <>
      <footer>
        <p>
          <Link to="/">Home</Link> | <Link to="/about">About Us</Link> |{" "}
          <Link to="/impressum">Impressum</Link>
        </p>
        <p>
          Copyright &copy; 2022 <a href="/">Chat History Analyzer</a>. All
          rights reserved.
        </p>
      </footer>
    </>
  );
}
