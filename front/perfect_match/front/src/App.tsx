import React from 'react';
import { 
  Brain, 
  Target, 
  Zap, 
  Users, 
  TrendingUp, 
  CheckCircle, 
  ArrowRight, 
  Star,
  FileText,
  Search,
  BarChart3,
  Mail,
  Phone,
  MapPin
} from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="fixed top-0 w-full bg-white/95 backdrop-blur-sm border-b border-gray-200 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-2">
              <Brain className="h-8 w-8 text-blue-600" />
              <span className="text-xl font-bold text-gray-900">Matching IA</span>
            </div>
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#features" className="text-gray-600 hover:text-blue-600 transition-colors">Fonctionnalités</a>
              <a href="#how-it-works" className="text-gray-600 hover:text-blue-600 transition-colors">Comment ça marche</a>
              <a href="#testimonials" className="text-gray-600 hover:text-blue-600 transition-colors">Témoignages</a>
              <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                Commencer
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-24 pb-16 bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
              Maximisez vos chances avec le
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600"> Matching IA</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
              Notre intelligence artificielle analyse votre CV et les offres d'emploi pour vous proposer 
              des candidatures parfaitement adaptées et optimisées.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-700 transition-all hover:scale-105 flex items-center justify-center space-x-2">
                <span>Analyser mon CV</span>
                <ArrowRight className="h-5 w-5" />
              </button>
              <button className="border border-gray-300 text-gray-700 px-8 py-4 rounded-lg font-semibold hover:bg-gray-50 transition-colors">
                Voir la démo
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600 mb-2">85%</div>
              <div className="text-gray-600">Taux de réussite amélioré</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-purple-600 mb-2">2.3x</div>
              <div className="text-gray-600">Plus de réponses positives</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-orange-600 mb-2">50k+</div>
              <div className="text-gray-600">Candidatures optimisées</div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Une IA qui comprend vos ambitions
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Découvrez comment notre technologie révolutionne la recherche d'emploi
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition-shadow">
              <div className="bg-blue-100 p-3 rounded-lg w-fit mb-4">
                <Target className="h-6 w-6 text-blue-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Matching Précis</h3>
              <p className="text-gray-600">
                Notre IA analyse en profondeur votre profil et identifie les opportunités 
                qui correspondent parfaitement à vos compétences et aspirations.
              </p>
            </div>

            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition-shadow">
              <div className="bg-purple-100 p-3 rounded-lg w-fit mb-4">
                <Zap className="h-6 w-6 text-purple-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Optimisation Automatique</h3>
              <p className="text-gray-600">
                Vos candidatures sont automatiquement adaptées pour chaque offre, 
                mettant en valeur les compétences les plus pertinentes.
              </p>
            </div>

            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition-shadow">
              <div className="bg-orange-100 p-3 rounded-lg w-fit mb-4">
                <TrendingUp className="h-6 w-6 text-orange-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Suivi Performance</h3>
              <p className="text-gray-600">
                Analysez vos résultats et recevez des recommandations personnalisées 
                pour améliorer continuellement vos candidatures.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* How it Works Section */}
      <section id="how-it-works" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Comment ça marche ?
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              3 étapes simples pour transformer votre recherche d'emploi
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-blue-600 text-white rounded-full w-12 h-12 flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                1
              </div>
              <div className="bg-blue-50 p-6 rounded-lg mb-4">
                <FileText className="h-8 w-8 text-blue-600 mx-auto mb-2" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Téléchargez votre CV</h3>
              <p className="text-gray-600">
                Importez votre CV et laissez notre IA analyser vos compétences, 
                expériences et objectifs professionnels.
              </p>
            </div>

            <div className="text-center">
              <div className="bg-purple-600 text-white rounded-full w-12 h-12 flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                2
              </div>
              <div className="bg-purple-50 p-6 rounded-lg mb-4">
                <Search className="h-8 w-8 text-purple-600 mx-auto mb-2" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Matching Intelligent</h3>
              <p className="text-gray-600">
                Notre algorithme scanne des milliers d'offres et identifie 
                celles qui correspondent le mieux à votre profil.
              </p>
            </div>

            <div className="text-center">
              <div className="bg-orange-600 text-white rounded-full w-12 h-12 flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                3
              </div>
              <div className="bg-orange-50 p-6 rounded-lg mb-4">
                <BarChart3 className="h-8 w-8 text-orange-600 mx-auto mb-2" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">Optimisation & Suivi</h3>
              <p className="text-gray-600">
                Recevez des candidatures optimisées et suivez vos performances 
                pour maximiser vos chances de succès.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section id="testimonials" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Ils ont transformé leur recherche d'emploi
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-xl shadow-sm">
              <div className="flex items-center mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                ))}
              </div>
              <p className="text-gray-600 mb-4">
                "Grâce à Matching IA, j'ai trouvé le poste de mes rêves en seulement 3 semaines. 
                L'optimisation automatique des candidatures fait vraiment la différence."
              </p>
              <div className="flex items-center">
                <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center mr-3">
                  <span className="text-blue-600 font-semibold">SL</span>
                </div>
                <div>
                  <div className="font-semibold text-gray-900">Sarah Legrand</div>
                  <div className="text-sm text-gray-600">Développeuse Full Stack</div>
                </div>
              </div>
            </div>

            <div className="bg-white p-8 rounded-xl shadow-sm">
              <div className="flex items-center mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                ))}
              </div>
              <p className="text-gray-600 mb-4">
                "L'IA a identifié des opportunités que je n'aurais jamais trouvées seul. 
                Mon taux de réponse a été multiplié par 3 !"
              </p>
              <div className="flex items-center">
                <div className="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center mr-3">
                  <span className="text-purple-600 font-semibold">MD</span>
                </div>
                <div>
                  <div className="font-semibold text-gray-900">Marc Dubois</div>
                  <div className="text-sm text-gray-600">Chef de Projet Digital</div>
                </div>
              </div>
            </div>

            <div className="bg-white p-8 rounded-xl shadow-sm">
              <div className="flex items-center mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="h-5 w-5 text-yellow-400 fill-current" />
                ))}
              </div>
              <p className="text-gray-600 mb-4">
                "Interface intuitive et résultats impressionnants. 
                Je recommande vivement cette solution à tous les chercheurs d'emploi."
              </p>
              <div className="flex items-center">
                <div className="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center mr-3">
                  <span className="text-orange-600 font-semibold">AM</span>
                </div>
                <div>
                  <div className="font-semibold text-gray-900">Alice Martin</div>
                  <div className="text-sm text-gray-600">Responsable Marketing</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-purple-600">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
            Prêt à transformer votre recherche d'emploi ?
          </h2>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Rejoignez des milliers de candidats qui ont déjà optimisé leur recherche avec notre IA
          </p>
          <button className="bg-white text-blue-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition-colors inline-flex items-center space-x-2">
            <span>Commencer maintenant</span>
            <ArrowRight className="h-5 w-5" />
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <Brain className="h-8 w-8 text-blue-400" />
                <span className="text-xl font-bold">Matching IA</span>
              </div>
              <p className="text-gray-400">
                L'intelligence artificielle au service de votre carrière professionnelle.
              </p>
            </div>
            
            <div>
              <h3 className="text-lg font-semibold mb-4">Produit</h3>
              <ul className="space-y-2">
                <li><a href="#" className="text-gray-400 hover:text-white transition-colors">Fonctionnalités</a></li>
                <li><a href="#" className="text-gray-400 hover:text-white transition-colors">Tarifs</a></li>
                <li><a href="#" className="text-gray-400 hover:text-white transition-colors">API</a></li>
              </ul>
            </div>
            
            <div>
              <h3 className="text-lg font-semibold mb-4">Support</h3>
              <ul className="space-y-2">
                <li><a href="#" className="text-gray-400 hover:text-white transition-colors">Centre d'aide</a></li>
                <li><a href="#" className="text-gray-400 hover:text-white transition-colors">Contact</a></li>
                <li><a href="#" className="text-gray-400 hover:text-white transition-colors">Blog</a></li>
              </ul>
            </div>
            
            <div>
              <h3 className="text-lg font-semibold mb-4">Contact</h3>
              <ul className="space-y-2">
                <li className="flex items-center space-x-2">
                  <Mail className="h-4 w-4 text-gray-400" />
                  <span className="text-gray-400">contact@matching-ia.com</span>
                </li>
                <li className="flex items-center space-x-2">
                  <Phone className="h-4 w-4 text-gray-400" />
                  <span className="text-gray-400">+33 1 23 45 67 89</span>
                </li>
                <li className="flex items-center space-x-2">
                  <MapPin className="h-4 w-4 text-gray-400" />
                  <span className="text-gray-400">Paris, France</span>
                </li>
              </ul>
            </div>
          </div>
          
          <div className="border-t border-gray-800 mt-12 pt-8 text-center text-gray-400">
            <p>&copy; 2024 Matching IA. Tous droits réservés.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;