import { createWebHistory, createRouter } from "vue-router";
import Home from "../components/Home.vue";
import SearchResult from "../components/SearchResult.vue";
import SearchFavorite from "../components/SearchFavorite.vue";
import SearchHistory from "../components/SearchHistory.vue";
import SearchNav from "../components/SearchNav.vue";

const router = createRouter({
    history : createWebHistory(),
    routes : [ // path별 component를 추가한다.
        { path : "/", name : "home", component : Home },
        {
            path: "/searchresult",  
            name: "SearchResult",  
            component: SearchResult,
        },
        {
            path: "/favorites",
            name: "Favorites",
            component: SearchFavorite,
            meta: { requiresAuth: true } 
        },
        {
            path: "/history",
            name: "SearchHistory",
            component: SearchHistory,
            meta: { requiresAuth: true } 
        },
        {
            path: "/Nav",
            name: "Nav",
            component: SearchNav,
            meta: { requiresAuth: true } 
        },
    ]
});

router.beforeEach((to, from, next) => {
    const isLoggedIn = localStorage.getItem('userToken') // 로그인 상태 확인
    if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
        //인증이 필요한 페이지에 접근하려고 할 때 로그인되어있지 않을때
        if (to.name === 'home') {
            // Home.vue에서 로그아웃한 경우 그대로 Home.vue
            next('/')
        }
        // 아니면 searchresult 페이지로 이동
        else {
            next('/searchresult')
        }
    } else {
        next()
    }
});

export default router;

