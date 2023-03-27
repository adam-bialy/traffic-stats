import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { AuthContextProvider } from "./store/auth-context";
import Main from "./components/Main";

function App() {
  return (
    <div className="App">
      <AuthContextProvider>
        <Header />
        <Main />
        <Footer />
      </AuthContextProvider>
    </div>
  );
}

export default App;
