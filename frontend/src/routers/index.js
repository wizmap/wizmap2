import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/Home.vue";
import Search from "../components/Search.vue";
import SearchResult from "../components/SearchResult.vue";
import SearchFavorite from "../components/SearchFavorite.vue";
import SearchHistory from "../components/SearchHistory.vue";

const router = createRouter({
    history : createWebHistory(),
    routes : [ // path별 component를 추가한다.
        { path : "/", name : "home", component : Home },
        {
            path: "/search",  // Search.vue로 이동할 Path
            name: "Search",  // router name
            component: Search,  // Path로 이동될 Component
        },
        {
            path: "/searchresult",  
            name: "SearchResult",  
            component: SearchResult,  
        },
        {
            path: "/favorites",
            name: "Favorites",
            component: SearchFavorite,
        },
        {
            path: "/history",
            name: "SearchHistory",
            component: SearchHistory,
        },
    ]
});

export default router;

