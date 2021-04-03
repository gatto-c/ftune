// BrowserRouter is the router implementation for HTML5 browsers (vs Native).
// Link is your replacement for anchor tags.
// Route is the conditionally shown component based on matching a path to a URL.
// Switch returns only the first matching route rather than all matching routes.
import { BrowserRouter as Router, Link, Route, Switch } from "react-router-dom";
import React from "react";
import MainCalcs from "./ftuneMainCalc.js";

const Home = () => <h1>Forza Tune</h1>;
const About = () => <h1>About...</h1>;

// We give each route either a target `component`, or we can send functions in `render` or `children`
// that return valid nodes. `children` always returns the given node whether there is a match or not.
const App = () => (
  <Router>
    <div>
      <Link to="/">Home</Link> <Link to={{ pathname: "/about" }}>About</Link>{" "}
      <Link to="/contact">Contact</Link> <Link to="/maincalcs">Main Calcs</Link>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/contact" render={() => <h1>Contact Us</h1>} />
        <Route path="/maincalcs" component={MainCalcs} />
        <Route render={() => <h1>Page not found</h1>} />
      </Switch>
    </div>
  </Router>
);

export default App;
